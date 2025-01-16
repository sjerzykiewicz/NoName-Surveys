<script lang="ts">
	import { XL } from '$lib/stores/global';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let members: {
		email: string;
		has_public_key: boolean;
	}[];
	export let selectedMembersToRemove: string[] = [];

	$: memberEmails = members.map((m) => m.email);

	$: allSelected =
		selectedMembersToRemove.length === memberEmails.length && selectedMembersToRemove.length > 0;

	function toggleAll() {
		selectedMembersToRemove = allSelected ? [] : [...memberEmails];
	}

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

{#if members.length === 0}
	<div title={$t('group_members')} class="title empty"><Tx text="no_members_yet" /></div>
{:else}
	<div title={$t('members_guide_title')} class="info">
		<div class="info-text">
			<Tx text="members_guide" />
		</div>
	</div>
	<table>
		<tr>
			<th title={$t('select_all')} class="checkbox-entry" class:disabled={members.length === 0}
				><label
					><input
						type="checkbox"
						disabled={members.length === 0}
						on:change={toggleAll}
						checked={allSelected}
					/></label
				></th
			>
			<th title={$t('keys_info_title')} id="info-header"><i class="symbol">encrypted</i></th>
			<th title={$t('group_members')} id="title-header"><Tx text="group_members" /></th>
		</tr>
		{#each members as member}
			<tr>
				<td title="{$t('select')} {member.email}" class="checkbox-entry"
					><label>
						<input type="checkbox" bind:group={selectedMembersToRemove} value={member.email} />
					</label></td
				>
				<td class="info-entry tooltip">
					{#if member.has_public_key}
						<i class="symbol">key</i>
						<span class="tooltip-text {innerWidth <= $XL ? 'right' : 'left'}"
							><Tx text="user_has_keys" /></span
						>
					{:else}
						<i class="symbol">key_off</i>
						<span class="tooltip-text {innerWidth <= $XL ? 'right' : 'left'}"
							><Tx text="user_has_no_keys" /></span
						>
					{/if}
				</td>
				<td title={member.email} class="basic-entry">{member.email}</td>
			</tr>
		{/each}
	</table>
{/if}

<style>
	.info {
		padding-bottom: 0.5em;
	}
</style>
