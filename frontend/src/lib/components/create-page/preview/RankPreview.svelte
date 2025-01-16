<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';
	import Tx from 'sveltekit-translate/translate/tx.svelte';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let questionIndex: number;

	let dontAnswer = false;
	let choices = $questions[questionIndex].choices.slice();

	function moveChoiceUp(index: number) {
		const higher = choices[index - 1];
		choices[index - 1] = choices[index];
		choices[index] = higher;
	}

	function moveChoiceDown(index: number) {
		const lower = choices[index + 1];
		choices[index + 1] = choices[index];
		choices[index] = lower;
	}

	function toggleDontAnswer() {
		if (!dontAnswer) {
			choices = [];
		} else {
			choices = $questions[questionIndex].choices;
		}
		dontAnswer = !dontAnswer;
	}
</script>

<div class="choice-area display" transition:slide={{ duration: 200, easing: cubicInOut }}>
	{#each choices as choice, choiceIndex}
		<div
			title={$t('answer_no', { index: choiceIndex + 1 })}
			class="choice"
			transition:slide={{ duration: 200, easing: cubicInOut }}
		>
			<div class="rank">{choiceIndex + 1}.</div>
			<div class="arrows">
				<button
					title={$t('move_answer_up')}
					class="up"
					disabled={choiceIndex === 0}
					on:click={() => moveChoiceUp(choiceIndex)}
				>
					<i class="symbol">keyboard_arrow_up</i>
				</button>
				<button
					title={$t('move_answer_down')}
					class="down"
					disabled={choiceIndex === choices.length - 1}
					on:click={() => moveChoiceDown(choiceIndex)}
				>
					<i class="symbol">keyboard_arrow_down</i>
				</button>
			</div>
			<div class="choice-input display">
				{choice}
			</div>
		</div>
	{/each}
	{#if !$questions[questionIndex].required}
		<label title={$t('dont_answer')} class="choice dont-answer">
			<div class="checkbox">
				<input type="checkbox" checked={dontAnswer} on:click={toggleDontAnswer} />
			</div>
			<div class="choice-input display" class:selected={dontAnswer}>
				<Tx text="dont_answer" />
			</div>
		</label>
	{/if}
</div>

<style>
	.choice-input,
	.choice-input:hover {
		background-color: var(--primary-color-2);
		cursor: default;
	}

	.dont-answer {
		cursor: pointer;
	}

	.dont-answer .choice-input {
		background-color: var(--primary-color-1);
		cursor: pointer;
	}

	.dont-answer .choice-input:hover,
	.dont-answer .choice-input.selected:hover {
		background-color: var(--secondary-color-1);
	}

	.dont-answer .choice-input.selected {
		background-color: var(--secondary-color-2);
		border: 1px solid var(--accent-color-1);
		color: var(--accent-color-1);
	}
</style>
