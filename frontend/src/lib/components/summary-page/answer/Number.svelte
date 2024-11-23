<script lang="ts">
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	import Tx from 'sveltekit-translate/translate/tx.svelte';
	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let data: { answer: number; min_value: number; max_value: number };
</script>

{#if data.answer === null}
	<div title={$t('question_not_answered')} class="summary_no_answers">
		<Tx text="question_not_answered" />
	</div>
{:else}
	<div class="choice-area display slider">
		<div title={$t('answer')} class="choice slider">
			<input
				class="limit-input"
				type="number"
				autocomplete="off"
				value={data.answer.toFixed(2)}
				disabled
			/>
		</div>
		<div class="limits">
			<div title={$t('minimum_value')} class="limit">{data.min_value}</div>
			<div title={$t('maximum_value')} class="limit">{data.max_value}</div>
		</div>
	</div>
{/if}

<style>
	.limit-input {
		color: var(--accent-color-1);
		border: 1px solid var(--accent-color-1);
		width: 100%;
		cursor: default;
		transition:
			0.2s,
			outline 0s;
	}
</style>
