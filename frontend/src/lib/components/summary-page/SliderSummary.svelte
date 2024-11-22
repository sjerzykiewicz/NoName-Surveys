<script lang="ts">
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let data: { answers: number[]; min_value: number; max_value: number };

	let existingAnswers = data.answers.filter((x) => x !== null);

	let avg =
		existingAnswers.length !== 0
			? (existingAnswers.reduce((a, b) => a + b, 0) / existingAnswers.length).toFixed(2)
			: $t('no_answers_to_question');
</script>

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

<style>
	.choice .limit {
		color: var(--accent-color-1);
		transition:
			0.2s,
			outline 0s;
	}
</style>
