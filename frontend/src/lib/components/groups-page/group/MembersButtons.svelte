<script lang="ts">
	import { goto, invalidateAll } from '$app/navigation';
	import { page } from '$app/stores';
	import MultiSelect from '$lib/components/MultiSelect.svelte';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { GroupError } from '$lib/entities/GroupError';
	import MembersError from '../MembersError.svelte';
	import { scrollToElement } from '$lib/utils/scrollToElement';
	import { tick } from 'svelte';

	export let members: string[];
	export let notMembers: string[];
	export let selectedMembersToRemove: string[] = [];
	export let group: string;

	let isPanelVisible: boolean = false;
	let selectedMembersToAdd: string[] = [];
	let membersError: GroupError = GroupError.NoError;

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
			body: JSON.stringify({ user_email: $page.data.session?.user?.email, name: group }),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (!deleteResponse.ok) {
			const body = await deleteResponse.json();
			alert(body.detail);
			return;
		}

		const newMembers = members.concat(selectedMembersToAdd);

		const createResponse = await fetch('/api/groups/create', {
			method: 'POST',
			body: JSON.stringify({
				user_email: $page.data.session?.user?.email,
				user_group_name: group,
				user_group_members: newMembers
			}),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (!createResponse.ok) {
			const body = await createResponse.json();
			alert(body.detail);
			return;
		}

		selectedMembersToAdd = [];
		isPanelVisible = false;
		invalidateAll();
	}

	async function removeMembers() {
		const deleteResponse = await fetch('/api/groups/delete', {
			method: 'POST',
			body: JSON.stringify({ user_email: $page.data.session?.user?.email, name: group }),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (!deleteResponse.ok) {
			const body = await deleteResponse.json();
			alert(body.detail);
			return;
		}

		if (selectedMembersToRemove.length === members.length) {
			goto('/groups', { replaceState: true, invalidateAll: true });
			return;
		}

		const newMembers = members.filter(
			(member: string) => !selectedMembersToRemove.includes(member)
		);

		const createResponse = await fetch('/api/groups/create', {
			method: 'POST',
			body: JSON.stringify({
				user_email: $page.data.session?.user?.email,
				user_group_name: group,
				user_group_members: newMembers
			}),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (!createResponse.ok) {
			const body = await createResponse.json();
			alert(body.detail);
			return;
		}

		selectedMembersToRemove = [];
		invalidateAll();
	}
</script>

<div class="button-row">
	<button
		title={isPanelVisible ? 'Stop adding group members' : 'Add group members'}
		class="add-group"
		class:clicked={isPanelVisible}
		on:click={togglePanel}
	>
		<i class="material-symbols-rounded">add</i>Members
	</button>
	{#if isPanelVisible}
		<div class="users-panel" transition:slide={{ duration: 200, easing: cubicInOut }}>
			<div title="Select members" class="select-list">
				<MultiSelect
					bind:selected={selectedMembersToAdd}
					options={notMembers}
					placeholder="Select members"
				/>
			</div>
			<button title="Finish adding group members" class="save" on:click={addMembers}>
				<i class="material-symbols-rounded">done</i>Apply
			</button>
		</div>
	{/if}
</div>
{#if isPanelVisible}
	<MembersError members={selectedMembersToAdd} error={membersError} margin={8.5} />
{/if}
<div class="button-row">
	<button
		title="Remove selected group members"
		disabled={selectedMembersToRemove.length === 0}
		on:click={removeMembers}
	>
		<i class="material-symbols-rounded">delete</i>Members
	</button>
</div>

<style>
	.button-row {
		display: flex;
		flex-flow: row wrap;
		align-items: flex-start;
		justify-content: flex-start;
		align-content: space-between;
		font-size: 1.25em;
		margin-top: 0.5em;
	}

	.users-panel {
		display: flex;
		flex: 1;
		align-items: flex-start;
	}

	.select-list {
		font-size: 0.8em;
		margin-right: 0.625em;
		margin-bottom: 0em;
	}

	button i {
		margin-right: 0.15em;
	}

	.save i {
		font-variation-settings: 'wght' 700;
	}

	@media screen and (max-width: 768px) {
		.button-row {
			font-size: 1em;
		}
	}
</style>
