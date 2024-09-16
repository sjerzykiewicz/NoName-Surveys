<script lang="ts">
	import type { LayoutServerData } from './$types';
	import { invalidateAll } from '$app/navigation';
	import { page } from '$app/stores';
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import GroupsTable from '$lib/components/groups-page/GroupsTable.svelte';
	import MultiSelect from 'svelte-multiselect';
	import { handleNewLine } from '$lib/utils/handleNewLine';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	export let data: LayoutServerData;

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

<Header>
	<div class="title">Your groups</div>
</Header>

<Content>
	<GroupsTable groups={data.group_list} />
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
			<div title="Select users" class="user-list">
				<MultiSelect
					bind:selected={groupMembers}
					options={data.user_list}
					--sms-max-width="100%"
					--sms-min-height="2.2em"
					--sms-border="1px solid var(--border-color)"
					--sms-border-radius="5px"
					--sms-bg="var(--secondary-dark-color)"
					--sms-selected-bg="var(--primary-color)"
					--sms-active-color="var(--text-color)"
					--sms-li-active-bg="var(--secondary-color)"
					--sms-text-color="var(--text-color)"
					--sms-open-z-index="0"
					--sms-options-max-height="16.5em"
					--sms-options-border="1px solid var(--border-color)"
					--sms-options-border-radius="5px"
					--sms-options-border-width="1px"
					--sms-options-bg="var(--primary-color)"
					--sms-options-shadow="0px 4px 4px var(--shadow-color)"
					--sms-remove-btn-hover-color="var(--error-color)"
					--sms-remove-btn-hover-bg="var(--secondary-color)"
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
	{/if}
</Content>

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

	.user-list {
		flex: 1;
		box-shadow: 0px 4px 4px var(--shadow-color);
		font-size: 0.8em;
		margin-right: 0.625em;
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

	.add-group i,
	.save i {
		margin-right: 0.15em;
		font-variation-settings: 'wght' 700;
	}

	@media screen and (max-width: 767px) {
		.button-row {
			font-size: 1em;
		}
	}
</style>
