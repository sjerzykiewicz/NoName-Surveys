<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let questionIndex: number;

	let value: number = NaN;

	function handleChange() {
		if (value !== null && !isNaN(value)) {
			if (value < parseFloat($questions[questionIndex].choices[0])) {
				value = parseFloat($questions[questionIndex].choices[0]);
			} else if (value > parseFloat($questions[questionIndex].choices[1])) {
				value = parseFloat($questions[questionIndex].choices[1]);
			} else {
				value = Math.round(value);
			}
		} else {
			value = NaN;
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
			bind:value
			on:input={handleChange}
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
</style>
