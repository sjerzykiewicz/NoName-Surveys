<script lang="ts">
	import { invalidateAll, goto } from '$app/navigation';
	import { page } from '$app/stores';

	export let groups: string[];

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
</script>

<table>
	<tr>
		<th title="Group title" id="title-header" colspan="3">Group Title</th>
	</tr>
	{#each groups as group}
		<tr>
			<td title="Rename the group" class="delete-entry"
				><i class="material-symbols-rounded">edit</i></td
			>
			<td title="Open the group" class="title-entry" on:click={() => goto('/groups/' + group)}
				>{group}</td
			>
			<td title="Delete the group" class="delete-entry" on:click={() => deleteGroup(group)}>
				<i class="material-symbols-rounded">delete</i></td
			>
		</tr>
	{/each}
</table>
