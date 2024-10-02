<script lang="ts">
	import { invalidateAll } from '$app/navigation';
	import { page } from '$app/stores';
	import MultiSelect from '$lib/components/MultiSelect.svelte';
	import { handleNewLine } from '$lib/utils/handleNewLine';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	export let users: string[];

	let isPanelVisible: boolean = false;
	let groupName: string = '';
	let groupMembers: string[] = [];

	function togglePanel() {
		isPanelVisible = !isPanelVisible;
	}

	function createGroup(user_group_name: string, user_group_members: string[]) {
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
	<div class="button-row" transition:slide={{ duration: 200, easing: cubicInOut }}>
		<div title="Select users" class="select-list">
			<MultiSelect bind:selected={groupMembers} options={users} placeholder="Select users" />
		</div>
		<button
			title="Save the group"
			class="save"
			on:click={() => createGroup(groupName, groupMembers)}
		>
			<i class="material-symbols-rounded">done</i>Create
		</button>
	</div>
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

	.save i {
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
