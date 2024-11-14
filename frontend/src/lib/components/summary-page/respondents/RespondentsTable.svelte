<script lang="ts">
	import PageButtons from '$lib/components/global/PageButtons.svelte';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let respondents;
	export let numRespondents;
</script>

{#if respondents.length === 0}
	<div title={$t('possible_respondents')} class="title empty">
		<Tx text="possible_respondents_empty"></Tx>
	</div>
{:else}
	<table>
		<tr>
			<th title={$t('possible_respondents')} id="title-header"
				><Tx text="possible_respondents"></Tx></th
			>
		</tr>
		{#each respondents as respondent}
			<tr>
				<td title={respondent} class="basic-entry">{respondent}</td>
			</tr>
		{/each}
	</table>
	<div class="button-row">
		<PageButtons numEntries={numRespondents} />
	</div>
{/if}

<style>
	.button-row {
		justify-content: flex-end;
	}

	@media screen and (max-width: 768px) {
		.button-row {
			font-size: 0.9em;
		}
	}
</style>
