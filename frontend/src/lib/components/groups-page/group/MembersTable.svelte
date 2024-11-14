<script lang="ts">
	import { XL } from '$lib/stores/global';
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
	<div title="Group members" class="title empty">No group members yet!</div>
{:else}
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
			<th title="Keys information" id="info-header"><i class="symbol">encrypted</i></th>
			<th title="Group members" id="title-header">Group Members</th>
		</tr>
		{#each members as member}
			<tr>
				<td title="Select {member.email}" class="checkbox-entry"
					><label>
						<input type="checkbox" bind:group={selectedMembersToRemove} value={member.email} />
					</label></td
				>
				<td class="info-entry tooltip">
					{#if member.has_public_key}
						<i class="symbol">key</i>
						<span class="tooltip-text {innerWidth <= $XL ? 'right' : 'left'}"
							>This user has already generated his keys.</span
						>
					{:else}
						<i class="symbol">key_off</i>
						<span class="tooltip-text {innerWidth <= $XL ? 'right' : 'left'}"
							>This user has not generated his keys yet.</span
						>
					{/if}
				</td>
				<td title={member.email} class="basic-entry">{member.email}</td>
			</tr>
		{/each}
	</table>
{/if}
