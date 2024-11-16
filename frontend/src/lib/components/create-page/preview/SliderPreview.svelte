<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let questionIndex: number;

	let value: number = parseFloat(
		(
			Math.round(
				Math.round(
					(parseFloat($questions[questionIndex].choices[0]) +
						parseFloat($questions[questionIndex].choices[1])) /
						2
				) / parseFloat($questions[questionIndex].choices[2])
			) * parseFloat($questions[questionIndex].choices[2])
		).toFixed(3)
	);

	function handleChange() {
		if (value !== null) {
			if (value < parseFloat($questions[questionIndex].choices[0])) {
				value = parseFloat($questions[questionIndex].choices[0]);
			} else if (value > parseFloat($questions[questionIndex].choices[1])) {
				value = parseFloat($questions[questionIndex].choices[1]);
			} else if (value % parseFloat($questions[questionIndex].choices[2]) !== 0) {
				value =
					Math.round(value / parseFloat($questions[questionIndex].choices[2])) *
					parseFloat($questions[questionIndex].choices[2]);
			}
			value = parseFloat(value.toFixed(3));
		}
	}
</script>

<div class="choice-area display slider" transition:slide={{ duration: 200, easing: cubicInOut }}>
	<div class="choice slider">
		<input
			title={$t('selected_value')}
			class="limit-input"
			type="number"
			autocomplete="off"
			min={$questions[questionIndex].choices[0]}
			max={$questions[questionIndex].choices[1]}
			step={$questions[questionIndex].choices[2]}
			name={questionIndex.toString()}
			bind:value
			on:change={handleChange}
		/>
	</div>
	<div title={$t('select_answer')} class="slider-area">
		<input
			class="range"
			type="range"
			min={$questions[questionIndex].choices[0]}
			max={$questions[questionIndex].choices[1]}
			step={$questions[questionIndex].choices[2]}
			name={questionIndex.toString()}
			bind:value
			on:change={handleChange}
		/>
	</div>
	<div class="limits">
		<div title={$t('minimum_value')} class="limit">{$questions[questionIndex].choices[0]}</div>
		<div title={$t('maximum_value')} class="limit">{$questions[questionIndex].choices[1]}</div>
	</div>
</div>

<style>
	.limit-input {
		width: 100%;
	}

	.range {
		background: var(--text-color-1);
		cursor: pointer;
	}

	.range:hover {
		background: var(--border-color-1);
	}

	.range::-webkit-slider-thumb {
		background: var(--accent-color-1);
		cursor: grab;
	}

	.range::-moz-range-thumb {
		background: var(--accent-color-1);
		cursor: grab;
	}

	.range::-webkit-slider-thumb:hover {
		background: var(--accent-color-2);
	}

	.range::-moz-range-thumb:hover {
		background: var(--accent-color-2);
	}

	.range::-webkit-slider-thumb:active {
		cursor: grabbing;
	}

	.range::-moz-range-thumb:active {
		cursor: grabbing;
	}
</style>
