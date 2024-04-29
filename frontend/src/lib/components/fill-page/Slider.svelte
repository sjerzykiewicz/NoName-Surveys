<script lang="ts">
	import { questions } from '$lib/stores/fill-page';
	import { answers } from '$lib/stores/fill-page';
	export let questionIndex: number;
	let value: number = parseFloat($questions[questionIndex].choices[0]);
	$answers[questionIndex].choices[0] = value.toString();
</script>

<div class="choice-area">
	<div class="slider">
		<input
			class="range"
			type="range"
			step="1"
			required={$questions[questionIndex].required}
			min={$questions[questionIndex].choices[0]}
			max={$questions[questionIndex].choices[1]}
			name={$questions[questionIndex].question}
			bind:value
			on:change={() => ($answers[questionIndex].choices[0] = value.toString())}
		/>
	</div>
	<div class="limits">
		<div title="Minimum value" class="limit">{$questions[questionIndex].choices[0]}</div>
		<div title="Current value" class="limit">{value}</div>
		<div title="Maximum value" class="limit">{$questions[questionIndex].choices[1]}</div>
	</div>
</div>

<style>
	.choice-area {
		display: flex;
		flex-flow: column;
		align-items: center;
		justify-content: center;
		font-size: 1em;
		font-weight: normal;
		font-family: 'Jura';
		color: #eaeaea;
		width: 86%;
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
		background: #999999;
		outline: none;
		opacity: 1;
		margin-left: 2.75em;
	}

	.range::-webkit-slider-thumb {
		appearance: none;
		width: 1.5em;
		height: 1.5em;
		border-radius: 1.5em;
		background: #eaeaea;
		cursor: default;
	}

	.range::-moz-range-thumb {
		appearance: none;
		width: 1.5em;
		height: 1.5em;
		border-radius: 1.5em;
		background: #eaeaea;
		cursor: default;
	}

	.limits {
		display: flex;
		align-items: center;
		justify-content: space-between;
		width: 100%;
	}

	.limit {
		background-color: #1a1a1a;
		padding: 0.25em;
		border: 1px solid #999999;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		font-size: 1.25em;
		font-weight: normal;
		font-family: 'Jura';
		color: #eaeaea;
		cursor: text;
		overflow: hidden;
		margin-left: 1.75em;
	}

	@media screen and (max-width: 767px) {
		.choice-area,
		.limit {
			font-size: 1em;
		}
	}
</style>
