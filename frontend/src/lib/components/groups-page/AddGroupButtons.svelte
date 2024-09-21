<script lang="ts">
	import { invalidateAll } from '$app/navigation';
	import { page } from '$app/stores';
	import MultiSelect from '$lib/components/MultiSelect.svelte';
	import { handleNewLine } from '$lib/utils/handleNewLine';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { tick } from 'svelte';
	import { scrollToElement } from '$lib/utils/scrollToElement';
	import Error from '$lib/components/groups-page/Error.svelte';

	export let users: string[];

	let isPanelVisible: boolean = false;
	let groupName: string = '';
	let groupMembers: string[] = [];
	let nameError: boolean = false;
	let membersError: boolean = false;

	function togglePanel() {
		isPanelVisible = !isPanelVisible;
		nameError = false;
		membersError = false;
	}

	async function checkCorrectness(name: string, members: string[]) {
		nameError = false;
		const n = name;
		if (n === null || n === undefined || n.length === 0) {
			nameError = true;
		}

		membersError = false;
		const m = members;
		if (m === null || m === undefined || m.length === 0) {
			membersError = true;
		}

		if (nameError) {
			await tick();
			scrollToElement('.group-input');
			return false;
		}

		if (membersError) {
			await tick();
			scrollToElement('.select-list');
			return false;
		}

		return true;
	}

	async function createGroup(user_group_name: string, user_group_members: string[]) {
		if (!(await checkCorrectness(user_group_name, user_group_members))) return;

		fetch('/api/groups/create', {
			method: 'POST',
			body: JSON.stringify({
				user_email: $page.data.session?.user?.email,
				user_group_name: user_group_name,
				user_group_members: user_group_members
			}),
			headers: {
				'Content-Type': 'application/json'
			}
		})
			.then(() => {
				groupName = '';
				groupMembers = [];
				isPanelVisible = false;
				invalidateAll();
			})
			.catch(() => alert('Error deleting group'));
	}
</script>

<div class="button-row">
	<button
		title={isPanelVisible ? 'Stop creating a group' : 'Create a group'}
		class="add-group"
		class:clicked={isPanelVisible}
		on:click={togglePanel}
	>
		<i class="material-symbols-rounded">add</i>Group
	</button>
	{#if isPanelVisible}
		<!-- svelte-ignore a11y-autofocus -->
		<div
			title="Enter a group name"
			class="group-input"
			contenteditable
			bind:textContent={groupName}
			autofocus
			role="textbox"
			tabindex="0"
			on:keydown={handleNewLine}
			transition:slide={{ duration: 200, easing: cubicInOut }}
		>
			{groupName}
		</div>
	{/if}
</div>
{#if isPanelVisible}
	<Error id="name" data={groupName} error={nameError} message="Please enter group name." />
	<div class="button-row" transition:slide={{ duration: 200, easing: cubicInOut }}>
		<div title="Select group members" class="select-list">
			<MultiSelect
				bind:selected={groupMembers}
				options={users}
				placeholder="Select group members"
				maxSelect={null}
			/>
		</div>
		<button
			title="Save the group"
			class="save"
			on:click={() => createGroup(groupName, groupMembers)}
		>
			<i class="material-symbols-rounded">done</i>Create
		</button>
	</div>
	<Error
		id="members"
		data={groupMembers}
		error={membersError}
		message="Please select group members."
	/>
{/if}

<style>
	.group-input {
		margin: 0em;
	}

	.group-input[contenteditable]:empty::before {
		content: 'Enter group name...';
		color: var(--text-dark-color);
	}

	.button-row {
		display: flex;
		flex-flow: row wrap;
		align-items: flex-start;
		justify-content: flex-start;
		align-content: space-between;
		font-size: 1.25em;
		margin-top: 0.5em;
	}

	.select-list {
		font-size: 0.8em;
		margin-right: 0.625em;
		margin-bottom: 0em;
	}

	.add-group {
		margin-right: 0.5em;
		transition:
			background-color 0.2s,
			color 0.2s;
	}

	.add-group.clicked {
		background-color: var(--accent-color);
		color: var(--text-color-2);
	}

	.add-group.clicked:hover {
		background-color: var(--accent-dark-color);
	}

	.add-group.clicked:active {
		background-color: var(--border-color);
	}

	.add-group.clicked i {
		transform: rotate(45deg);
	}

	.add-group i,
	.save i {
		margin-right: 0.15em;
		font-variation-settings: 'wght' 700;
		transform: rotate(0deg);
		transition: transform 0.2s;
	}

	@media screen and (max-width: 767px) {
		.button-row {
			font-size: 1em;
		}
	}
</style>
