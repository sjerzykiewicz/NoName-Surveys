<script lang="ts">
	import { invalidateAll } from '$app/navigation';
	import { page } from '$app/stores';
	import MultiSelect from '$lib/components/MultiSelect.svelte';
	import { handleNewLine } from '$lib/utils/handleNewLine';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { tick } from 'svelte';
	import { scrollToElement } from '$lib/utils/scrollToElement';
	import { GroupError } from '$lib/entities/GroupError';
	import MembersError from '$lib/components/groups-page/MembersError.svelte';
	import NameError from '$lib/components/groups-page/NameError.svelte';
	import { LIMIT_OF_CHARS } from '$lib/stores/global';
	import { limitInput } from '$lib/utils/limitInput';

	export let groups: string[];
	export let users: string[];

	let isPanelVisible: boolean = false;
	let groupName: string = '';
	let groupMembers: string[] = [];
	let nameError: GroupError = GroupError.NoError;
	let membersError: GroupError = GroupError.NoError;

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
		} else if (groups.some((g) => g === n)) {
			nameError = GroupError.NameNonUnique;
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
		<div
			class="input-container"
			class:max={groupName.length >= $LIMIT_OF_CHARS}
			transition:slide={{ duration: 200, easing: cubicInOut }}
		>
			<!-- svelte-ignore a11y-autofocus -->
			<div
				title="Enter a group name"
				class="group-input"
				contenteditable
				bind:textContent={groupName}
				autofocus
				role="textbox"
				tabindex="0"
				on:keydown={(e) => {
					handleNewLine(e);
					limitInput(e, groupName, $LIMIT_OF_CHARS);
				}}
			>
				{groupName}
			</div>
			<span class="char-count">{groupName.length} / {$LIMIT_OF_CHARS}</span>
		</div>
	{/if}
</div>
{#if isPanelVisible}
	<NameError name={groupName.trim()} error={nameError} {groups} />
	<div class="button-row" transition:slide={{ duration: 200, easing: cubicInOut }}>
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
			on:click={() => createGroup(groupName.trim(), groupMembers)}
		>
			<i class="material-symbols-rounded">done</i>Create
		</button>
	</div>
	<MembersError members={groupMembers} error={membersError} />
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

	.input-container {
		margin-bottom: -1.4em;
	}

	@media screen and (max-width: 767px) {
		.button-row {
			font-size: 1em;
		}
	}
</style>
