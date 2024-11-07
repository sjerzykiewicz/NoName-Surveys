<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { M } from '$lib/stores/global';
	import { afterUpdate } from 'svelte';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	export let questionIndex: number;

	let innerWidth: number;
	let min: number = -999999999999;
	let max: number = 999999999999;

	let value: number = Math.round(
		(parseFloat($questions[questionIndex].choices[0]) +
			parseFloat($questions[questionIndex].choices[1])) /
			2
	);

	function handleChange(value: number, i: number) {
		if (isNaN(value) || value === null || value === undefined) {
			$questions[questionIndex].choices[i] = '';
		} else if (value < min) {
			$questions[questionIndex].choices[i] = min.toString();
		} else if (value > max) {
			$questions[questionIndex].choices[i] = max.toString();
		}
	}

	afterUpdate(() => {
		value = Math.round(
			(parseFloat($questions[questionIndex].choices[0]) +
				parseFloat($questions[questionIndex].choices[1])) /
				2
		);
	});
</script>

<svelte:window bind:innerWidth />

<div class="choice-area slider" transition:slide={{ duration: 200, easing: cubicInOut }}>
	<div class="slider-area">
		<input
			class="range"
			type="range"
			step="1"
			min={$questions[questionIndex].choices[0]}
			max={$questions[questionIndex].choices[1]}
			name={questionIndex.toString()}
			disabled
			bind:value
		/>
	</div>
	<div class="limits">
		<label>
			Minimum
			<input
				title="Enter minimum value"
				class="limit-input"
				type="number"
				{min}
				{max}
				name={questionIndex.toString()}
				autocomplete="off"
				placeholder={innerWidth <= $M ? 'Enter min...' : 'Enter minimum value...'}
				bind:value={$questions[questionIndex].choices[0]}
				on:keydown|once={() => ($questions[questionIndex].choices[0] = '')}
				on:change={() => handleChange(parseFloat($questions[questionIndex].choices[0]), 0)}
			/></label
		>
		<label>
			Maximum
			<input
				title="Enter maximum value"
				class="limit-input"
				type="number"
				{min}
				{max}
				name={questionIndex.toString()}
				autocomplete="off"
				placeholder={innerWidth <= $M ? 'Enter max...' : 'Enter maximum value...'}
				bind:value={$questions[questionIndex].choices[1]}
				on:keydown|once={() => ($questions[questionIndex].choices[1] = '')}
				on:change={() => handleChange(parseFloat($questions[questionIndex].choices[1]), 1)}
			/></label
		>
	</div>
</div>

<style>
	label {
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	@media screen and (max-width: 768px) {
		.limit-input {
			width: 6em;
		}
	}
</style>
