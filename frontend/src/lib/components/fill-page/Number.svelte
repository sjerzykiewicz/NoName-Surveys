<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	import Tx from 'sveltekit-translate/translate/tx.svelte';
	export let questionIndex: number;

	let value: number;

	function handleClear() {
		value = NaN;
		$answers[questionIndex].choices = [];
	}

	function handleChange() {
		if (value !== null) {
			if (value < parseFloat($questions[questionIndex].choices[0])) {
				value = parseFloat($questions[questionIndex].choices[0]);
			} else if (value > parseFloat($questions[questionIndex].choices[1])) {
				value = parseFloat($questions[questionIndex].choices[1]);
			} else {
				value = Math.round(value);
			}
			$answers[questionIndex].choices[0] = value.toString();
		}
	}
</script>

<div class="choice-area display slider">
	<div class="choice slider">
		<input
			title={$t('selected_value')}
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
	<div class="limits">
		<div title={$t('minimum_value')} class="limit">{$questions[questionIndex].choices[0]}</div>
		<div title={$t('maximum_value')} class="limit">{$questions[questionIndex].choices[1]}</div>
	</div>
	{#if !isNaN(value)}
		<div class="clear_answer">
			<button title={$t('clear_answer_title')} on:click={handleClear}
				><Tx text="clear_answer" /></button
			>
		</div>
	{/if}
</div>

<style>
	.limit-input {
		width: 100%;
	}
</style>
