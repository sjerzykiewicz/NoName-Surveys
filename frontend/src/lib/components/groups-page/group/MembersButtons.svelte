<script lang="ts">
	import { goto, invalidateAll } from '$app/navigation';
	import MultiSelect from '$lib/components/global/MultiSelect.svelte';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { GroupError } from '$lib/entities/GroupError';
	import MembersError from '$lib/components/groups-page/MembersError.svelte';
	import { scrollToElement } from '$lib/utils/scrollToElement';
	import { tick } from 'svelte';
	import { errorModalContent, isErrorModalHidden } from '$lib/stores/global';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import DeleteModal from '$lib/components/global/DeleteModal.svelte';
	import { page } from '$app/stores';
	import PageButtons from '$lib/components/global/PageButtons.svelte';

	export let members: {
		email: string;
		has_public_key: boolean;
	}[];
	export let notMembers: string[];
	export let selectedMembersToRemove: string[] = [];
	export let group: string;
	export let numMembers: number;

	let isPanelVisible: boolean = false;
	let selectedMembersToAdd: string[] = [];
	let membersError: GroupError = GroupError.NoError;
	let isModalHidden: boolean = true;

	$: memberEmails = members.map((m) => m.email);

	function togglePanel() {
		isPanelVisible = !isPanelVisible;
		membersError = GroupError.NoError;
	}

	async function checkCorrectness(members: string[]) {
		membersError = GroupError.NoError;
		const m = members;
		if (m === null || m === undefined || m.length === 0) {
			membersError = GroupError.MembersRequired;
		}

		if (membersError !== GroupError.NoError) {
			await tick();
			scrollToElement('.select-list');
			return false;
		}

		return true;
	}

	async function addMembers() {
		if (!(await checkCorrectness(selectedMembersToAdd))) return;

		const deleteResponse = await fetch('/api/groups/delete', {
			method: 'POST',
			body: JSON.stringify({ name: group }),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (!deleteResponse.ok) {
			const body = await deleteResponse.json();
			$errorModalContent = getErrorMessage(body.detail);
			$isErrorModalHidden = false;
			return;
		}

		const newMembers = memberEmails.concat(selectedMembersToAdd);

		const createResponse = await fetch('/api/groups/create', {
			method: 'POST',
			body: JSON.stringify({
				user_group_name: group,
				user_group_members: newMembers
			}),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (!createResponse.ok) {
			const body = await createResponse.json();
			$errorModalContent = getErrorMessage(body.detail);
			$isErrorModalHidden = false;
			return;
		}

		selectedMembersToAdd = [];
		isPanelVisible = false;
		await invalidateAll();
	}

	async function removeMembers() {
		const deleteResponse = await fetch('/api/groups/delete', {
			method: 'POST',
			body: JSON.stringify({ name: group }),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (!deleteResponse.ok) {
			const body = await deleteResponse.json();
			$errorModalContent = getErrorMessage(body.detail);
			$isErrorModalHidden = false;
			return;
		}

		if (selectedMembersToRemove.length === members.length) {
			goto('/groups/' + $page.params.groupsPage, { replaceState: true, invalidateAll: true });
			return;
		}

		// TODO: go to previous page if there are no users left on the current page

		const selectedMembersToRemoveSet = new Set(selectedMembersToRemove);
		const newMembers = memberEmails.filter((m) => !selectedMembersToRemoveSet.has(m));

		const createResponse = await fetch('/api/groups/create', {
			method: 'POST',
			body: JSON.stringify({
				user_group_name: group,
				user_group_members: newMembers
			}),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (!createResponse.ok) {
			const body = await createResponse.json();
			$errorModalContent = getErrorMessage(body.detail);
			$isErrorModalHidden = false;
			return;
		}

		isModalHidden = true;
		selectedMembersToRemove = [];
		await invalidateAll();
	}
</script>

<DeleteModal
	title="Removing Group Members"
	bind:isHidden={isModalHidden}
	deleteEntries={removeMembers}
/>

<div class="button-row">
	<div class="button-sub-row">
		<button
			title={isPanelVisible ? 'Stop adding group members' : 'Add group members'}
			class="add-group"
			class:clicked={isPanelVisible}
			on:click={togglePanel}
		>
			<i class="symbol">add</i>Members
		</button>
		{#if members.length > 0}
			<button
				title="Remove selected group members"
				class="delete-group"
				disabled={selectedMembersToRemove.length === 0}
				on:click={() => (isModalHidden = false)}
			>
				<i class="symbol">delete</i>Delete
			</button>
		{/if}
	</div>
	<PageButtons numEntries={numMembers} />
</div>
{#if isPanelVisible}
	<div class="button-row" transition:slide={{ duration: 200, easing: cubicInOut }}>
		<div title="Select group members" class="select-list">
			<MultiSelect
				bind:selected={selectedMembersToAdd}
				options={notMembers}
				placeholder="Select group members"
			/>
		</div>
		<button title="Finish adding group members" class="save" on:click={addMembers}>
			<i class="symbol">done</i>Apply
		</button>
	</div>
	<MembersError members={selectedMembersToAdd} error={membersError} />
{/if}

<style>
	.save i {
		font-variation-settings: 'wght' 700;
	}
</style>
