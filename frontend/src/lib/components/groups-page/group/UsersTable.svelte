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

	tr:nth-child(2n + 1) td {
		background-color: var(--primary-dark-color);
	}

	tr:nth-child(2n + 2) td {
		background-color: var(--primary-color);
	}
</style>
