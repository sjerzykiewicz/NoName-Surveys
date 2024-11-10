<script lang="ts">
	import { page } from '$app/stores';
	import { XL } from '$lib/stores/global';

	export let users: string[];
	export let selectedUsersToRemove: string[] = [];

	let innerWidth: number;

	$: usersWithoutOwner = users.filter((user) => user !== $page.data.session?.user?.email);

	$: allSelected =
		selectedUsersToRemove.length === usersWithoutOwner.length && selectedUsersToRemove.length > 0;

	function toggleAll() {
		selectedUsersToRemove = allSelected ? [] : [...usersWithoutOwner];
	}
</script>

<svelte:window bind:innerWidth />

{#if users.length === 0}
	<div title="Users with access" class="title empty">No users with access to display!</div>
{:else}
	<table>
		<tr>
			<th title="Select all" class="checkbox-entry" class:disabled={usersWithoutOwner.length === 0}
				><label
					><input
						type="checkbox"
						disabled={usersWithoutOwner.length === 0}
						on:change={toggleAll}
						checked={allSelected}
					/></label
				></th
			>
			<th title="User type" id="info-header"><i class="symbol">person</i></th>
			<th title="Users with access" id="title-header">Users With Access</th>
		</tr>
		{#each users.toSorted() as user}
			<tr>
				<td
					title="Select {user}"
					class="checkbox-entry"
					class:disabled={user === $page.data.session?.user?.email}
					><label>
						<input
							type="checkbox"
							disabled={user === $page.data.session?.user?.email}
							bind:group={selectedUsersToRemove}
							value={user}
						/>
					</label></td
				>
				<td class="info-entry tooltip">
					{#if user === $page.data.session?.user?.email}
						<i class="symbol">verified</i>
						<span class="tooltip-text {innerWidth <= $XL ? 'right' : 'left'}">Owner.</span>
					{:else}
						<i class="symbol">share</i>
						<span class="tooltip-text {innerWidth <= $XL ? 'right' : 'left'}"
							>User with access.</span
						>
					{/if}
				</td>
				<td title={user} class="basic-entry">{user}</td>
			</tr>
		{/each}
	</table>
{/if}

<style>
	.tooltip {
		--tooltip-width: 9em;
	}
</style>
