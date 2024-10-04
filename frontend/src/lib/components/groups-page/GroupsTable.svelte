<script lang="ts">
	import { invalidateAll, goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { handleNewLine } from '$lib/utils/handleNewLine';
	import { tick } from 'svelte';
	import { scrollToElement } from '$lib/utils/scrollToElement';
	import { GroupError } from '$lib/entities/GroupError';
	import NameTableError from '$lib/components/groups-page/NameTableError.svelte';

	export let groups: string[];

	let editedIndex: number = -1;
	let newName: string = '';
	let nameError: GroupError = GroupError.NoError;

	async function checkCorrectness(name: string) {
		nameError = GroupError.NoError;
		const n = name;
		if (n === null || n === undefined || n.length === 0) {
			nameError = GroupError.NameRequired;
		} else if (groups.some((g) => g === n)) {
			nameError = GroupError.NameNonUnique;
		}

		if (nameError !== GroupError.NoError) {
			await tick();
			scrollToElement('.table-input');
			return false;
		}

		return true;
	}

	function deleteGroup(name: string, i: number) {
		fetch('/api/groups/delete', {
			method: 'POST',
			body: JSON.stringify({ user_email: $page.data.session?.user?.email, name: name }),
			headers: {
				'Content-Type': 'application/json'
			}
		})
			.then(() => {
				groups.splice(i, 1);
				invalidateAll();
			})
			.catch(() => alert('Error deleting group'));
	}

	async function renameGroup(name: string, new_name: string) {
		if (!(await checkCorrectness(new_name))) return;

		fetch('/api/groups/rename', {
			method: 'POST',
			body: JSON.stringify({
				user_email: $page.data.session?.user?.email,
				name: name,
				new_name: new_name
			}),
			headers: {
				'Content-Type': 'application/json'
			}
		})
			.then(() => {
				editedIndex = -1;
				newName = '';
				invalidateAll();
			})
			.catch(() => alert('Error renaming group'));
	}

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

{#if groups.length === 0}
	<div class="info-row">
		<div title="Groups" class="title empty">No groups yet!</div>
		<div class="tooltip">
			<i class="material-symbols-rounded">info</i>
			<span class="tooltip-text {innerWidth <= 423 ? 'bottom' : 'right'}">
				When creating a secure survey, you can choose a group of possible respondents. To create a
				group, click on the button below. All your created groups will be stored on this page.
			</span>
		</div>
	</div>
{:else}
	<table>
		<tr>
			<th title="Group title" id="title-header" colspan="3">Group Title</th>
		</tr>
		{#each groups as group, groupIndex}
			<tr>
				{#if editedIndex === groupIndex}
					<td
						title="Stop renaming the group"
						class="button-entry"
						on:click={() => {
							editedIndex = -1;
							newName = '';
							nameError = GroupError.NoError;
						}}><i class="material-symbols-rounded">edit_off</i></td
					>
					<td>
						<!-- svelte-ignore a11y-autofocus -->
						<div
							title="Enter a new group name"
							class="table-input"
							contenteditable
							bind:textContent={newName}
							autofocus={innerWidth > 767}
							role="textbox"
							tabindex="0"
							on:keydown={handleNewLine}
						>
							{newName}
						</div>
						<NameTableError name={newName} error={nameError} {groups} />
					</td>
					<td
						title="Save the new group name"
						class="button-entry save-entry"
						on:click={() => renameGroup(group, newName)}
					>
						<i class="material-symbols-rounded">save</i></td
					>
				{:else}
					<td
						title="Rename the group"
						class="button-entry"
						on:click={() => {
							editedIndex = groupIndex;
							nameError = GroupError.NoError;
						}}><i class="material-symbols-rounded">edit</i></td
					>
					<td title="Open the group" class="title-entry" on:click={() => goto('/groups/' + group)}
						>{group}</td
					>
					<td
						title="Delete the group"
						class="button-entry"
						on:click={() => deleteGroup(group, groupIndex)}
					>
						<i class="material-symbols-rounded">delete</i></td
					>
				{/if}
			</tr>
		{/each}
	</table>
{/if}

<style>
	.table-input {
		margin: 0em;
		overflow-wrap: anywhere;
	}

	.table-input[contenteditable]:empty::before {
		content: 'Enter group name...';
		color: var(--text-dark-color);
	}
	.save-entry {
		background-color: var(--accent-color);
	}

	.save-entry:hover {
		background-color: var(--accent-dark-color);
	}

	.save-entry:active {
		background-color: var(--border-color);
	}
</style>
