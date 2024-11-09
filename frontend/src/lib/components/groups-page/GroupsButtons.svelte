<script lang="ts">
	import { invalidateAll } from '$app/navigation';
	import MultiSelect from '$lib/components/global/MultiSelect.svelte';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { tick } from 'svelte';
	import { scrollToElement } from '$lib/utils/scrollToElement';
	import { GroupError } from '$lib/entities/GroupError';
	import MembersError from '$lib/components/groups-page/MembersError.svelte';
	import NameError from '$lib/components/groups-page/NameError.svelte';
	import { errorModalContent, isErrorModalHidden, LIMIT_OF_CHARS, M } from '$lib/stores/global';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import DeleteModal from '$lib/components/global/DeleteModal.svelte';
	import ImportEmails from '$lib/components/global/ImportEmails.svelte';
	import PageButtons from '$lib/components/global/PageButtons.svelte';
	import Input from '$lib/components/global/Input.svelte';

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
	let nameInput: HTMLDivElement;

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
	<div
		class="buttons-container"
		transition:slide={{ duration: 200, easing: cubicInOut }}
		on:introend={() => nameInput.focus()}
	>
		<div class="button-row">
			<Input
				bind:text={groupName}
				label="Group Name"
				title="Enter a group name"
				bind:element={nameInput}
				handleEnter={(e) => {
					if (e.key === 'Enter') {
						e.preventDefault();
						createGroup(groupName.trim(), groupMembers);
						e.stopImmediatePropagation();
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
			<div title="Select group members" class="select-list">
				<MultiSelect
					bind:selected={groupMembers}
					options={users}
					placeholder="Select group members"
				/>
			</div>
			<button
				title="Save the group"
				class="done"
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
		/>
	</div>
{/if}

<style>
	.buttons-container {
		padding: 0.2em;
		margin: -0.2em;
	}
</style>
