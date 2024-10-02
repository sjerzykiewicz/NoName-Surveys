<script lang="ts">
	import { page } from '$app/stores';

	export let users: string[];

	let innerWidth: number;

	function takeAwayAccess(user: string) {
		return user;
	}
</script>

<svelte:window bind:innerWidth />

<table>
	<tr>
		<th title="Users with access" id="title-header" colspan="3">Users With Access</th>
	</tr>
	{#each users as user}
		<tr>
			<td class="info-entry tooltip">
				{#if user === $page.data.session?.user?.email}
					<i class="material-symbols-rounded">verified</i>
					<span class="tooltip-text {innerWidth <= 1160 ? 'right' : 'left'}">Owner.</span>
				{:else}
					<i class="material-symbols-rounded">share</i>
					<span class="tooltip-text {innerWidth <= 1160 ? 'right' : 'left'}">User with access.</span
					>
				{/if}
			</td>
			<td
				title={user}
				class="title-entry"
				colspan={user === $page.data.session?.user?.email ? 2 : 1}>{user}</td
			>
			{#if user !== $page.data.session?.user?.email}
				<td title="Take away access" class="button-entry" on:click={() => takeAwayAccess(user)}>
					<i class="material-symbols-rounded">delete</i></td
				>
			{/if}
		</tr>
	{/each}
</table>

<style>
	.tooltip {
		--tooltip-width: 9em;
	}

	.title-entry {
		cursor: default;
	}

	tr:nth-child(2n + 1) td {
		background-color: var(--primary-dark-color);
	}

	tr:nth-child(2n + 2) td {
		background-color: var(--primary-color);
	}

	.button-entry:hover {
		background-color: var(--secondary-color);
	}
</style>
