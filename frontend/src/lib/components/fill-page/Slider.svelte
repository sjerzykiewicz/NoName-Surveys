<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';

	export let questionIndex: number;

	let value: number = Math.round(
		(parseFloat($questions[questionIndex].choices[0]) +
			parseFloat($questions[questionIndex].choices[1])) /
			2
	);

	$answers[questionIndex].choices[0] = value.toString();

	function handleChange() {
		if (value !== null) {
			if (value < parseFloat($questions[questionIndex].choices[0])) {
				value = parseFloat($questions[questionIndex].choices[0]);
			} else if (value > parseFloat($questions[questionIndex].choices[1])) {
				value = parseFloat($questions[questionIndex].choices[1]);
			}
			$answers[questionIndex].choices[0] = value.toString();
		}
	}
</script>

<div class="choice-area display slider">
	<div class="choice slider">
		<input
			title="Selected value"
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
	<div title="Select your answer" class="slider-area">
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
		<div title="Minimum value" class="limit">{$questions[questionIndex].choices[0]}</div>
		<div title="Maximum value" class="limit">{$questions[questionIndex].choices[1]}</div>
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
