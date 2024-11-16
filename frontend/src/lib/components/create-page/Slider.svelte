<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { M } from '$lib/stores/global';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let questionIndex: number;

	let innerWidth: number;
	let min: number = -999999999999;
	let max: number = 999999999999;

	function handleChange(value: number, i: number, min: number, max: number) {
		if (isNaN(value) || value === null || value === undefined) {
			$questions[questionIndex].choices[i] = '';
		} else if (value < min) {
			$questions[questionIndex].choices[i] = min.toString();
		} else if (value > max) {
			$questions[questionIndex].choices[i] = max.toString();
		}
	}
</script>

<svelte:window bind:innerWidth />

<div class="choice-area slider" transition:slide={{ duration: 200, easing: cubicInOut }}>
	<div class="slider-area">
		<input class="range" type="range" name={questionIndex.toString()} disabled />
	</div>
	<div class="limits">
		<label class="min">
			<Tx text="minimum" />
			<input
				title={$t('number_min_title')}
				class="limit-input"
				type="number"
				{min}
				{max}
				name={questionIndex.toString()}
				autocomplete="off"
				placeholder={innerWidth <= $M
					? $t('number_min_placeholder_short')
					: $t('number_min_placeholder')}
				bind:value={$questions[questionIndex].choices[0]}
				on:keydown|once={() => ($questions[questionIndex].choices[0] = '')}
				on:change={() =>
					handleChange(parseFloat($questions[questionIndex].choices[0]), 0, min, max)}
			/></label
		>
		<label class="step">
			<Tx text="precision" />
			<input
				title={$t('slider_precision_title')}
				class="limit-input"
				type="number"
				min="0"
				{max}
				name={questionIndex.toString()}
				autocomplete="off"
				placeholder={innerWidth <= $M
					? $t('slider_precision_placeholder_short')
					: $t('slider_precision_placeholder')}
				bind:value={$questions[questionIndex].choices[2]}
				on:keydown|once={() => ($questions[questionIndex].choices[2] = '')}
				on:change={() =>
					handleChange(parseFloat($questions[questionIndex].choices[2]), 2, 0.001, max)}
			/></label
		>
		<label class="max">
			<Tx text="maximum" />
			<input
				title={$t('number_max_title')}
				class="limit-input"
				type="number"
				{min}
				{max}
				name={questionIndex.toString()}
				autocomplete="off"
				placeholder={innerWidth <= $M
					? $t('number_max_placeholder_short')
					: $t('number_max_placeholder')}
				bind:value={$questions[questionIndex].choices[1]}
				on:keydown|once={() => ($questions[questionIndex].choices[1] = '')}
				on:change={() =>
					handleChange(parseFloat($questions[questionIndex].choices[1]), 1, min, max)}
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

	.limit-input {
		width: 9em;
	}

	@media screen and (max-width: 768px) {
		.limit-input {
			width: 6em;
		}
	}

	@media screen and (max-width: 425px) {
		.limits {
			flex-wrap: wrap;
			justify-content: space-around;
		}

		.min {
			order: 0;
		}

		.max {
			order: 1;
		}

		.step {
			order: 2;
			margin-top: 0.75em;
		}
	}

	@media screen and (max-width: 320px) {
		.limits {
			flex-direction: column;
			flex-wrap: nowrap;
		}

		.limit-input {
			width: 9em;
		}

		.min {
			order: 0;
		}

		.step {
			order: 1;
			margin-top: 0.75em;
		}

		.max {
			order: 2;
			margin-top: 0.75em;
		}
	}
</style>
