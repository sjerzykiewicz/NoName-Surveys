<script lang="ts">
	import { page } from '$app/stores';
	import { XL } from '$lib/stores/global';
	import { getContext } from 'svelte';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

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
	<div title={$t('users_with_access')} class="title empty">
		<Tx text="no_surveys_with_access" />
	</div>
{:else}
	<div title={$t('access_guide_title')} class="info">
		<div class="info-text">
			<Tx text="access_guide" />
		</div>
	</div>
	<table>
		<tr>
			<th
				title={$t('select_all')}
				class="checkbox-entry"
				class:disabled={usersWithoutOwner.length === 0}
				><label
					><input
						type="checkbox"
						disabled={usersWithoutOwner.length === 0}
						on:change={toggleAll}
						checked={allSelected}
					/></label
				></th
			>
			<th title={$t('user_type')} id="info-header"><i class="symbol">person</i></th>
			<th title={$t('users_with_access')} id="title-header"><Tx text="users_with_access" /></th>
		</tr>
		{#each users as user}
			<tr>
				<td
					title="{$t('select')} {user}"
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
						<span class="tooltip-text {innerWidth <= $XL ? 'right' : 'left'}"
							><Tx text="owner" />.</span
						>
					{:else}
						<i class="symbol">share</i>
						<span class="tooltip-text {innerWidth <= $XL ? 'right' : 'left'}"
							><Tx text="user_with_access" />.</span
						>
					{/if}
				</td>
				<td title={user} class="basic-entry">{user}</td>
			</tr>
		{/each}
	</table>
{/if}

<style>
	.info {
		padding-bottom: 0.5em;
	}

	.tooltip {
		--tooltip-width: 9em;
	}
</style>
