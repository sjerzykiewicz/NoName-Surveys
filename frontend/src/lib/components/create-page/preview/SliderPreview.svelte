<script lang="ts">
	import { questions } from '$lib/stores/create-page';

	export let questionIndex: number;

	let value: number = Math.round(
		(parseFloat($questions[questionIndex].choices[0]) +
			parseFloat($questions[questionIndex].choices[1])) /
			2
	);
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
			name={questionIndex.toString()}
			bind:value
		/>
	</div>
	<div title="Select your answer" class="slider-area">
		<input
			class="range"
			type="range"
			step="1"
			min={$questions[questionIndex].choices[0]}
			max={$questions[questionIndex].choices[1]}
			name={questionIndex.toString()}
			bind:value
		/>
	</div>
	<div class="limits">
		<div title="Minimum value" class="limit">{$questions[questionIndex].choices[0]}</div>
		<div title="Maximum value" class="limit">{$questions[questionIndex].choices[1]}</div>
	</div>
</div>

<style>
	.limit-input {
		color: var(--accent-color);
		border: 1px solid var(--accent-color);
		width: 15em;
	}

	.range {
		background: var(--text-color);
		cursor: pointer;
	}

	.range:hover {
		background: var(--border-color);
	}

	.range::-webkit-slider-thumb {
		background: var(--accent-color);
		cursor: grab;
	}

	.range::-moz-range-thumb {
		background: var(--accent-color);
		cursor: grab;
	}

	.range::-webkit-slider-thumb:hover {
		background: var(--accent-dark-color);
	}

	.range::-moz-range-thumb:hover {
		background: var(--accent-dark-color);
	}

	.range::-webkit-slider-thumb:active {
		cursor: grabbing;
	}

	.range::-moz-range-thumb:active {
		cursor: grabbing;
	}

	@media screen and (max-width: 767px) {
		.limit-input {
			width: 10em;
		}
	}
</style>
