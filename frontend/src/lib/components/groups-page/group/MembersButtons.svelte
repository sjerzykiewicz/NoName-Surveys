<script lang="ts">
	import { goto, invalidateAll } from '$app/navigation';
	import MultiSelect from '$lib/components/global/MultiSelect.svelte';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { GroupError } from '$lib/entities/GroupError';
	import MembersError from '$lib/components/groups-page/MembersError.svelte';
	import { scrollToElement } from '$lib/utils/scrollToElement';
	import { ENTRIES_PER_PAGE, errorModalContent, isErrorModalHidden, M } from '$lib/stores/global';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import DeleteModal from '$lib/components/global/DeleteModal.svelte';
	import { page } from '$app/stores';
	import PageButtons from '$lib/components/global/PageButtons.svelte';
	import { changePage } from '$lib/utils/changePage';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';
	import ImportEmails from '$lib/components/global/ImportEmails.svelte';
	import WarningModal from '$lib/components/global/WarningModal.svelte';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let members: {
		email: string;
		has_public_key: boolean;
	}[];
	export let notMembers: string[];
	export let selectedMembersToRemove: string[] = [];
	export let group: string;
	export let numMembers: number;
	export let invalidEmails: string[] = [];
	export let isExportButtonVisible: boolean = false;

	let isPanelVisible: boolean = false;
	let selectedMembersToAdd: string[] = [];
	let membersError: GroupError = GroupError.NoError;
	let isModalHidden: boolean = true;

	function togglePanel() {
		isPanelVisible = !isPanelVisible;
		membersError = GroupError.NoError;
	}

	function checkCorrectness(members: string[]) {
		membersError = GroupError.NoError;
		const m = members;
		if (m === null || m === undefined || m.length === 0) {
			membersError = GroupError.MembersRequired;
		}

		if (membersError !== GroupError.NoError) {
			scrollToElement('.select-list');
			return false;
		}

		return true;
	}

	async function addMembers() {
		if (!checkCorrectness(selectedMembersToAdd)) return;

		const response = await fetch('/api/groups/members/add', {
			method: 'POST',
			body: JSON.stringify({
				name: group,
				users: selectedMembersToAdd
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

		selectedMembersToAdd = [];
		isPanelVisible = false;
		await invalidateAll();
	}

	async function removeMembers() {
		if (selectedMembersToRemove.length >= numMembers) {
			const response = await fetch('/api/groups/delete', {
				method: 'POST',
				body: JSON.stringify({ names: [group] }),
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

			await goto('/groups/' + $page.params.groupsPage, {
				replaceState: true,
				invalidateAll: true
			});
			return;
		}

		const response = await fetch('/api/groups/members/delete', {
			method: 'POST',
			body: JSON.stringify({
				name: group,
				users: selectedMembersToRemove
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

		const currentPage = parseInt($page.params.groupPage);
		const maxPage = Math.ceil(numMembers / $ENTRIES_PER_PAGE) - 1;
		if (
			selectedMembersToRemove.length >= members.length &&
			currentPage >= maxPage &&
			currentPage > 0
		) {
			await changePage($page.url.pathname, currentPage - 1);
		}

		isModalHidden = true;
		selectedMembersToRemove = [];
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
	title={$t('removing_group_members')}
	bind:isHidden={isModalHidden}
	deleteEntries={removeMembers}
/>

<div class="button-row top-row">
	<div class="button-sub-row">
		<button
			title={isPanelVisible ? $t('add_group_members_stop') : $t('add_group_members')}
			class="add-group"
			class:clicked={isPanelVisible}
			on:click={togglePanel}
		>
			<i class="symbol">add</i><Tx text="members" />
		</button>
		{#if members.length > 0}
			<button
				title={$t('remove_group_members')}
				class="delete-group"
				disabled={selectedMembersToRemove.length === 0}
				on:click={() => (isModalHidden = false)}
			>
				<i class="symbol">delete</i><Tx text="delete" />
			</button>
		{/if}
	</div>
	<PageButtons numEntries={numMembers} />
</div>
{#if isPanelVisible}
	<div class="buttons-container" transition:slide={{ duration: 200, easing: cubicInOut }}>
		<div class="button-row">
			<div title={$t('select_group_members')} class="select-list">
				<MultiSelect
					bind:selected={selectedMembersToAdd}
					options={notMembers}
					placeholder={$t('select_group_members')}
				/>
			</div>
			<button title={$t('add_members_finish')} class="done" on:click={addMembers}>
				<i class="symbol">done</i><Tx text="submit" />
			</button>
		</div>
		<MembersError members={selectedMembersToAdd} error={membersError} />
		<ImportEmails
			bind:users={selectedMembersToAdd}
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
