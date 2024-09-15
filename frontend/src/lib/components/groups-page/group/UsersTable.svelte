<script lang="ts">
	export let users: string[];
</script>

<table>
	<tr>
		<th title="Users" id="title-header">Users</th>
	</tr>
	{#each users as user}
		<tr>
			<td title={user} class="title-entry">{user}</td>
		</tr>
	{/each}
</table>

<style>
	.title-entry {
		cursor: default;
	}

	.title-entry:hover,
	.title-entry:active {
		background-color: initial;
	}
</style>
