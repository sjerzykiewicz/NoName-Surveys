<script lang="ts">
	import { invalidateAll } from '$app/navigation';
	import MultiSelect from '$lib/components/global/MultiSelect.svelte';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { scrollToElement } from '$lib/utils/scrollToElement';
	import { GroupError } from '$lib/entities/GroupError';
	import MembersError from '$lib/components/groups-page/MembersError.svelte';
	import NameError from '$lib/components/groups-page/NameError.svelte';
	import {
		ENTRIES_PER_PAGE,
		errorModalContent,
		isErrorModalHidden,
		isWarningModalHidden,
		LIMIT_OF_CHARS,
		LIMIT_OF_GROUPS,
		M,
		warningModalContent
	} from '$lib/stores/global';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import DeleteModal from '$lib/components/global/DeleteModal.svelte';
	import ImportEmails from '$lib/components/global/ImportEmails.svelte';
	import PageButtons from '$lib/components/global/PageButtons.svelte';
	import Input from '$lib/components/global/Input.svelte';
	import { page } from '$app/stores';
	import { changePage } from '$lib/utils/changePage';
	import WarningModal from '$lib/components/global/WarningModal.svelte';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let groups: {
		user_group_name: string;
		all_members_have_public_keys: true;
	}[];
	export let users: string[];
	export let numGroups: number;
	export let selectedGroupsToRemove: string[] = [];
	export let invalidEmails: string[] = [];
	export let isExportButtonVisible: boolean = false;

	let isPanelVisible: boolean = false;
	let groupName: string = '';
	let groupMembers: string[] = [];
	let nameError: GroupError = GroupError.NoError;
	let membersError: GroupError = GroupError.NoError;
	let isModalHidden: boolean = true;
	let nameInput: HTMLDivElement;
	let isSubmitButtonDisabled: boolean = false;

	$: groupNames = groups.map((g) => g.user_group_name);

	function togglePanel() {
		isPanelVisible = !isPanelVisible;
		nameError = GroupError.NoError;
		membersError = GroupError.NoError;
	}

	function checkCorrectness(name: string, members: string[]) {
		nameError = GroupError.NoError;
		const n = name;
		if (n === null || n === undefined || n.length === 0) {
			nameError = GroupError.NameRequired;
		} else if (n.length > $LIMIT_OF_CHARS) {
			nameError = GroupError.NameTooLong;
		} else if (groupNames.some((g) => g === n)) {
			nameError = GroupError.NameNonUnique;
		} else if (n.match(/^[\p{L}\p{N} /-]+$/u) === null) {
			nameError = GroupError.NameInvalid;
		}

		membersError = GroupError.NoError;
		const m = members;
		if (m === null || m === undefined || m.length === 0) {
			membersError = GroupError.MembersRequired;
		}

		if (nameError !== GroupError.NoError) {
			scrollToElement('.group-input');
			return false;
		}

		if (membersError !== GroupError.NoError) {
			scrollToElement('.select-list');
			return false;
		}

		return true;
	}

	async function createGroup() {
		if (numGroups >= $LIMIT_OF_GROUPS) {
			isExportButtonVisible = false;
			$warningModalContent = $t('max_groups_reached');
			$isWarningModalHidden = false;
			return;
		}

		const name = groupName.trim();

		if (!checkCorrectness(name, groupMembers)) return;

		const response = await fetch('/api/groups/create', {
			method: 'POST',
			body: JSON.stringify({
				user_group_name: name,
				user_group_members: groupMembers
			}),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (!response.ok) {
			const body = await response.json();
			$errorModalContent = getErrorMessage(body.detail);
			$isErrorModalHidden = false;
			return;
		}

		groupName = '';
		groupMembers = [];
		isPanelVisible = false;
		await invalidateAll();
	}

	async function deleteGroups() {
		const response = await fetch('/api/groups/delete', {
			method: 'POST',
			body: JSON.stringify({ names: selectedGroupsToRemove }),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (!response.ok) {
			const body = await response.json();
			$errorModalContent = getErrorMessage(body.detail);
			$isErrorModalHidden = false;
			return;
		}

		const currentPage = parseInt($page.params.groupsPage);
		const maxPage = Math.ceil(numGroups / $ENTRIES_PER_PAGE) - 1;
		if (
			selectedGroupsToRemove.length >= groups.length &&
			currentPage >= maxPage &&
			currentPage > 0
		) {
			await changePage($page.url.pathname, currentPage - 1);
		}

		isModalHidden = true;
		selectedGroupsToRemove = [];
		await invalidateAll();
	}

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

<WarningModal
	{isExportButtonVisible}
	emails={invalidEmails}
	--width-warning={innerWidth <= $M ? '20em' : '22em'}
/>

<DeleteModal
	title={$t('deleting_group')}
	bind:isHidden={isModalHidden}
	deleteEntries={deleteGroups}
/>

<div class="button-row top-row">
	<div class="button-sub-row">
		<button
			title={isPanelVisible ? $t('create_group_stop') : $t('create_group')}
			class="add-group"
			class:clicked={isPanelVisible}
			on:click={togglePanel}
		>
			<i class="symbol">add</i><Tx text="group" />
		</button>
		{#if groups.length > 0}
			<button
				title={$t('delete_selected_groups')}
				class="delete-group"
				disabled={selectedGroupsToRemove.length === 0}
				on:click={() => (isModalHidden = false)}
			>
				<i class="symbol">delete</i><Tx text="delete" />
			</button>
		{/if}
	</div>
	<PageButtons numEntries={numGroups} />
</div>
{#if isPanelVisible}
	<div
		class="buttons-container"
		transition:slide={{ duration: 200, easing: cubicInOut }}
		on:introend={() => nameInput.focus()}
	>
		<div class="button-row">
			<Input
				bind:text={groupName}
				label={$t('group_name')}
				title={$t('enter_group_name')}
				bind:element={nameInput}
				handleEnter={async (e) => {
					if (e.key === 'Enter') {
						e.preventDefault();
						e.stopImmediatePropagation();
						if (!isSubmitButtonDisabled) {
							isSubmitButtonDisabled = true;
							await createGroup();
							isSubmitButtonDisabled = false;
						}
					}
				}}
				--margin-right="0em"
				--char-count-left="6.5em"
				--container-margin="-0.9em"
			/>
		</div>
		<NameError
			name={groupName.trim()}
			error={nameError}
			groups={groupNames}
			--font-size={innerWidth <= $M ? '0.8em' : '1em'}
		/>
		<div class="button-row">
			<div title={$t('select_group_members')} class="select-list">
				<MultiSelect
					bind:selected={groupMembers}
					options={users}
					placeholder={$t('select_group_members')}
				/>
			</div>
			<button
				title={$t('save_group')}
				class="done"
				disabled={isSubmitButtonDisabled}
				on:click={async () => {
					isSubmitButtonDisabled = true;
					await createGroup();
					isSubmitButtonDisabled = false;
				}}
			>
				<i class="symbol">done</i><Tx text="submit" />
			</button>
		</div>
		<MembersError members={groupMembers} error={membersError} />
		<ImportEmails
			bind:users={groupMembers}
			title={$t('import_members_title')}
			label={$t('import_members_label')}
			checkKeys={false}
			bind:invalidEmails
			bind:isExportButtonVisible
		/>
	</div>
{/if}

<style>
	.buttons-container {
		padding: 0.2em;
		margin: -0.2em;
	}

	@media screen and (max-width: 768px) {
		.top-row {
			font-size: 0.9em;
		}
	}
</style>
