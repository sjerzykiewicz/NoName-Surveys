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

	function handleChange(value: number, i: number) {
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
	<div class="limits">
		<label class="min">
			<Tx text="minimum"></Tx>
			<input
				title={$t('create_number_min_title')}
				class="limit-input"
				type="number"
				{min}
				{max}
				name={questionIndex.toString()}
				autocomplete="off"
				placeholder={innerWidth <= $M
					? $t('create_number_min_placeholder_short')
					: $t('create_number_min_placeholder')}
				bind:value={$questions[questionIndex].choices[0]}
				on:keydown|once={() => ($questions[questionIndex].choices[0] = '')}
				on:change={() => handleChange(parseFloat($questions[questionIndex].choices[0]), 0)}
			/></label
		>
		<label class="max">
			<Tx text="maximum"></Tx>
			<input
				title={$t('create_number_max_title')}
				class="limit-input"
				type="number"
				{min}
				{max}
				name={questionIndex.toString()}
				autocomplete="off"
				placeholder={innerWidth <= $M
					? $t('create_number_max_placeholder_short')
					: $t('create_number_max_placeholder')}
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
			width: 9em;
		}
	}

	@media screen and (max-width: 425px) {
		.limits {
			flex-direction: column;
		}

		.max {
			margin-top: 0.75em;
		}
	}
</style>
