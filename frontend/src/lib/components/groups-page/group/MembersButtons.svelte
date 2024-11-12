<script lang="ts">
	import { goto, invalidateAll } from '$app/navigation';
	import MultiSelect from '$lib/components/global/MultiSelect.svelte';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { GroupError } from '$lib/entities/GroupError';
	import MembersError from '$lib/components/groups-page/MembersError.svelte';
	import { scrollToElement } from '$lib/utils/scrollToElement';
	import { tick } from 'svelte';
	import { ENTRIES_PER_PAGE, errorModalContent, isErrorModalHidden } from '$lib/stores/global';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import DeleteModal from '$lib/components/global/DeleteModal.svelte';
	import { page } from '$app/stores';
	import PageButtons from '$lib/components/global/PageButtons.svelte';
	import { changePage } from '$lib/utils/changePage';

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

		const response = await fetch('/api/groups/add-users', {
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

		const response = await fetch('/api/groups/remove-users', {
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
		<button title="Finish adding group members" class="done" on:click={addMembers}>
			<i class="symbol">done</i>Apply
		</button>
	</div>
	<MembersError members={selectedMembersToAdd} error={membersError} />
{/if}
