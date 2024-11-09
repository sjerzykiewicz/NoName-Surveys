<script lang="ts">
	import { invalidateAll } from '$app/navigation';
	import MultiSelect from '$lib/components/global/MultiSelect.svelte';
	import { handleNewLine } from '$lib/utils/handleNewLine';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { tick } from 'svelte';
	import { scrollToElement } from '$lib/utils/scrollToElement';
	import { GroupError } from '$lib/entities/GroupError';
	import MembersError from '$lib/components/groups-page/MembersError.svelte';
	import NameError from '$lib/components/groups-page/NameError.svelte';
	import { errorModalContent, isErrorModalHidden, LIMIT_OF_CHARS } from '$lib/stores/global';
	import { limitInput } from '$lib/utils/limitInput';
	import { M } from '$lib/stores/global';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import DeleteModal from '$lib/components/global/DeleteModal.svelte';
	import ImportEmails from '$lib/components/global/ImportEmails.svelte';
	import PageButtons from '$lib/components/global/PageButtons.svelte';

	export let groups: {
		user_group_name: string;
		all_members_have_public_keys: true;
	}[];
	export let users: string[];
	export let numGroups: number;
	export let selectedGroupsToRemove: string[] = [];

	let isPanelVisible: boolean = false;
	let groupName: string = '';
	let groupMembers: string[] = [];
	let nameError: GroupError = GroupError.NoError;
	let membersError: GroupError = GroupError.NoError;
	let isModalHidden: boolean = true;

	$: groupNames = groups.map((g) => g.user_group_name);

	function togglePanel() {
		isPanelVisible = !isPanelVisible;
		nameError = GroupError.NoError;
		membersError = GroupError.NoError;
	}

	async function checkCorrectness(name: string, members: string[]) {
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
			await tick();
			scrollToElement('.group-input');
			return false;
		}

		if (membersError !== GroupError.NoError) {
			await tick();
			scrollToElement('.select-list');
			return false;
		}

		return true;
	}

	async function createGroup(user_group_name: string, user_group_members: string[]) {
		if (!(await checkCorrectness(user_group_name, user_group_members))) return;

		const response = await fetch('/api/groups/create', {
			method: 'POST',
			body: JSON.stringify({
				user_group_name: user_group_name,
				user_group_members: user_group_members
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
		// TODO: fix and improve this
		selectedGroupsToRemove.forEach(async (group) => {
			const response = await fetch('/api/groups/delete', {
				method: 'POST',
				body: JSON.stringify({ name: group }),
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

			groups = groups.filter((g) => g.user_group_name !== group);
		});
		// TODO: go to previous page if there are no groups left on the current page

		isModalHidden = true;
		selectedGroupsToRemove = [];
		await invalidateAll();
	}

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

<DeleteModal title="Deleting Groups" bind:isHidden={isModalHidden} deleteEntries={deleteGroups} />

<div class="button-row">
	<div class="button-sub-row">
		<button
			title={isPanelVisible ? 'Stop creating a group' : 'Create a group'}
			class="add-group"
			class:clicked={isPanelVisible}
			on:click={togglePanel}
		>
			<i class="symbol">add</i>Group
		</button>
		{#if groups.length > 0}
			<button
				title="Delete selected groups"
				class="delete-group"
				disabled={selectedGroupsToRemove.length === 0}
				on:click={() => (isModalHidden = false)}
			>
				<i class="symbol">delete</i>Delete
			</button>
		{/if}
	</div>
	<PageButtons numEntries={numGroups} />
</div>
{#if isPanelVisible}
	<div class="buttons-container" transition:slide={{ duration: 200, easing: cubicInOut }}>
		<div class="button-row">
			<div
				class="input-container"
				class:max={groupName.length > $LIMIT_OF_CHARS}
				transition:slide={{ duration: 200, easing: cubicInOut }}
			>
				<!-- svelte-ignore a11y-autofocus -->
				<div
					title="Enter a group name"
					class="group-input"
					contenteditable
					bind:textContent={groupName}
					autofocus={innerWidth > $M}
					role="textbox"
					tabindex="0"
					on:keydown={(e) => {
						handleNewLine(e);
						limitInput(e, groupName, $LIMIT_OF_CHARS);
					}}
				></div>
				<span class="char-count">{groupName.length} / {$LIMIT_OF_CHARS}</span>
			</div>
		</div>
		<NameError name={groupName.trim()} error={nameError} groups={groupNames} />
		<div class="button-row">
			<div title="Select group members" class="select-list">
				<MultiSelect
					bind:selected={groupMembers}
					options={users}
					placeholder="Select group members"
				/>
			</div>
			<button
				title="Save the group"
				class="save"
				on:click={() => {
					createGroup(groupName.trim(), groupMembers);
				}}
			>
				<i class="symbol">done</i>Create
			</button>
		</div>
		<MembersError members={groupMembers} error={membersError} />
		<ImportEmails
			bind:users={groupMembers}
			title="Import group members from a .csv file"
			label="Or import group members from a .csv file."
			id="emails-file"
			checkKeys={false}
			--font-size-button="1.25em"
			--font-size-warning="0.8em"
		/>
	</div>
{/if}

<style>
	.buttons-container {
		padding: 0.2em;
		margin: -0.2em;
	}

	.group-input {
		margin: 0em;
	}

	.group-input[contenteditable]:empty::before {
		content: 'Enter group name...';
		color: var(--text-color-3);
	}

	.save i {
		font-variation-settings: 'wght' 700;
		transform: rotate(0deg);
		transition: transform 0.2s;
	}

	.input-container {
		margin-bottom: -1.4em;
	}

	@media screen and (max-width: 768px) {
		.button-row {
			font-size: 0.8em;
		}
	}
</style>
