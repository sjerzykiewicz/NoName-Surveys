<script lang="ts">
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	import Tx from 'sveltekit-translate/translate/tx.svelte';
	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let data: { answers: number[]; min_value: number; max_value: number };

	let existingAnswers = data.answers.filter((x) => x !== null);

	let avg =
		existingAnswers.length !== 0
			? (existingAnswers.reduce((a, b) => a + b, 0) / existingAnswers.length).toFixed(2)
			: 0;
</script>

{#if existingAnswers.length === 0}
	<div title={$t('no_answers_to_question')} class="summary-no-answers">
		<Tx text="no_answers_to_question" />
	</div>
{:else}
	<div class="choice-area display slider">
		<div class="choice slider">
			<div title={$t('average')} class="limit">{avg}</div>
		</div>
		<div title={$t('average')} class="slider-area">
			<input
				class="range"
				type="range"
				step="1"
				min={data.min_value}
				max={data.max_value}
				value={avg}
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
	.choice .limit {
		color: var(--accent-color-1);
		transition:
			0.2s,
			outline 0s;
	}
</style>
