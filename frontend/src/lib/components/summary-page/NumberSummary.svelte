<script lang="ts">
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let data: { answers: number[]; min_value: number; max_value: number };

	let avg = (data.answers.reduce((a, b) => a + b, 0) / data.answers.length).toFixed(2);
</script>

<div class="choice-area display slider">
	<div class="choice slider">
		<div title="Average" class="limit">{avg}</div>
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
