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

<div class="choice-area">
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
		<input
			title="Your answer"
			class="current-value"
			type="number"
			autocomplete="off"
			min={$questions[questionIndex].choices[0]}
			max={$questions[questionIndex].choices[1]}
			name={questionIndex.toString()}
			bind:value
			on:change={handleChange}
		/>
		<div title="Maximum value" class="limit">{$questions[questionIndex].choices[1]}</div>
	</div>
</div>

<style>
	.choice-area {
		display: flex;
		flex-flow: column;
		align-items: center;
		justify-content: center;
	}

	.slider {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 100%;
		margin-top: 0.5em;
		margin-bottom: 1em;
	}

	.range {
		appearance: none;
		width: 100%;
		height: 0.5em;
		border-radius: 0.5em;
		background: var(--text-color);
		outline: none;
		opacity: 1;
		margin-left: 2.75em;
		cursor: pointer;
	}

	.range:hover {
		background: var(--border-color);
	}

	.range::-webkit-slider-thumb {
		appearance: none;
		width: 1.5em;
		height: 1.5em;
		border-radius: 1.5em;
		background: var(--accent-color);
		cursor: grab;
	}

	.range::-moz-range-thumb {
		appearance: none;
		width: 1.5em;
		height: 1.5em;
		border-radius: 1.5em;
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

	.limits {
		display: flex;
		align-items: center;
		justify-content: space-between;
		width: 100%;
	}

	.limit {
		text-shadow: 0px 4px 4px var(--shadow-color);
		font-size: 1.25em;
		font-weight: bold;
		color: var(--text-color);
		cursor: default;
		margin-left: 2em;
	}

	.current-value {
		background-color: var(--secondary-dark-color);
		padding: 0.25em;
		border: 1px solid var(--border-color);
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--shadow-color);
		font-size: 1.25em;
		font-weight: normal;
		color: var(--text-color);
		cursor: text;
		overflow: hidden;
		width: 3.5em;
		margin-left: 2em;
	}

	@media screen and (max-width: 767px) {
		.choice-area,
		.limit,
		.current-value {
			font-size: 1em;
		}
	}
</style>
