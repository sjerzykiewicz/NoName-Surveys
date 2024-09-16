<script lang="ts">
	import { invalidateAll, goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { handleNewLine } from '$lib/utils/handleNewLine';

	export let groups: string[];

	let editedIndex: number = -1;
	let newName: string = '';

	function deleteGroup(name: string) {
		fetch('/api/groups/delete', {
			method: 'POST',
			body: JSON.stringify({ user_email: $page.data.session?.user?.email, name: name }),
			headers: {
				'Content-Type': 'application/json'
			}
		})
			.then(() => {
				groups.splice(groups.indexOf(name), 1);
				invalidateAll();
			})
			.catch(() => alert('Error deleting group'));
	}

	function renameGroup(name: string, new_name: string) {
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
</script>

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
					}}><i class="material-symbols-rounded">edit_off</i></td
				>
				<td>
					<!-- svelte-ignore a11y-autofocus -->
					<div
						title="Enter a new group name"
						class="table-input"
						contenteditable
						bind:textContent={newName}
						autofocus
						role="textbox"
						tabindex="0"
						on:keydown={handleNewLine}
					>
						{newName}
					</div>
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
					}}><i class="material-symbols-rounded">edit</i></td
				>
				<td title="Open the group" class="title-entry" on:click={() => goto('/groups/' + group)}
					>{group}</td
				>
				<td title="Delete the group" class="button-entry" on:click={() => deleteGroup(group)}>
					<i class="material-symbols-rounded">delete</i></td
				>
			{/if}
		</tr>
	{/each}
</table>

<style>
	.table-input {
		margin: 0em;
		overflow-wrap: anywhere;
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
