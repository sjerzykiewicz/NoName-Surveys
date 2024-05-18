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
		if (value < parseFloat($questions[questionIndex].choices[0])) {
			value = parseFloat($questions[questionIndex].choices[0]);
		} else if (value > parseFloat($questions[questionIndex].choices[1])) {
			value = parseFloat($questions[questionIndex].choices[1]);
		}
		$answers[questionIndex].choices[0] = value.toString();
	}
</script>

<div class="choice-area display">
	<div class="choice">
		<input
			title="Selected value"
			class="limit-input"
			type="number"
			autocomplete="off"
			min={$questions[questionIndex].choices[0]}
			max={$questions[questionIndex].choices[1]}
			name={questionIndex.toString()}
			bind:value
			on:change={handleChange}
		/>
	</div>
	<div class="slider">
		<input
			class="range"
			type="range"
			step="1"
			min={$questions[questionIndex].choices[0]}
			max={$questions[questionIndex].choices[1]}
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
	.choice-area {
		display: flex;
		flex-flow: column;
		align-items: center;
		justify-content: center;
		margin-left: 2.25em;
	}

	.choice {
		justify-content: center;
		width: calc(100% - 2.25em);
		margin-right: 2.25em;
	}

	.limit-input {
		color: var(--accent-color);
		border: 1px solid var(--accent-color);
	}

	.limit {
		text-shadow: 0px 4px 4px var(--shadow-color);
		font-weight: bold;
		color: var(--text-color);
		cursor: default;
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
		.choice-area,
		.limit {
			font-size: 1em;
		}

		.limit-input {
			width: 10em;
		}
	}
</style>
