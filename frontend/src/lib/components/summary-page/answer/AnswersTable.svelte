<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import PageButtons from '$lib/components/global/PageButtons.svelte';
	import { getContext } from 'svelte';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let numbers: Array<number>;

	$: currentPage = parseInt($page.url.pathname.substring($page.url.pathname.lastIndexOf('/') + 1));

	$: numbersPaginated = numbers.slice(currentPage * 10, currentPage * 10 + 10);
</script>

{#if numbersPaginated.length === 0}
	<div title={$t('number_of_answers')} class="title empty"><Tx text="no_answers_yet" /></div>
{:else}
	<table>
		<tr>
			<th title={$t('number_of_answers')} id="info-header"><i class="symbol">numbers</i></th>
			<th title={$t('answers')} id="title-header"><Tx text="answers" /></th>
		</tr>
		{#each numbersPaginated as i}
			<tr>
				<td title={$t('answer_no', { index: i + 1 })} class="info-entry">{i + 1}.</td>
				<td title={$t('view_answer_no', { index: i + 1 })} class="title-entry"
					><button on:click={() => goto($page.url.pathname + '/' + i)}><Tx text="answer" /></button
					></td
				>
			</tr>
		{/each}
	</table>
	<div class="button-row">
		<PageButtons numEntries={numbers.length} />
	</div>
{/if}

<style>
	.info-entry {
		width: 2.3em;
		text-align: center;
		font-weight: 700;
	}

	.button-row {
		justify-content: flex-end;
	}

	@media screen and (max-width: 768px) {
		.button-row {
			font-size: 0.9em;
		}
	}
</style>
