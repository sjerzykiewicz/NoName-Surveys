<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';
	import { slide } from 'svelte/transition';
	import { cubicInOut } from 'svelte/easing';

	import Tx from 'sveltekit-translate/translate/tx.svelte';
	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);
	export let questionIndex: number;

	let dontAnswer: boolean = false;
	$answers[questionIndex].choices = [...$questions[questionIndex].choices];

	function moveChoiceUp(index: number) {
		const higher = $answers[questionIndex].choices[index - 1];
		$answers[questionIndex].choices[index - 1] = $answers[questionIndex].choices[index];
		$answers[questionIndex].choices[index] = higher;
	}

	function moveChoiceDown(index: number) {
		const lower = $answers[questionIndex].choices[index + 1];
		$answers[questionIndex].choices[index + 1] = $answers[questionIndex].choices[index];
		$answers[questionIndex].choices[index] = lower;
	}

	function toggleDontAnswer() {
		if (!dontAnswer) {
			$answers[questionIndex].choices = [];
		} else {
			$answers[questionIndex].choices = [...$questions[questionIndex].choices];
		}
		dontAnswer = !dontAnswer;
	}
</script>

<div class="choice-area display">
	{#each $answers[questionIndex].choices as choice, choiceIndex}
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
					disabled={choiceIndex === 0 || dontAnswer}
					on:click={() => moveChoiceUp(choiceIndex)}
				>
					<i class="symbol">keyboard_arrow_up</i>
				</button>
				<button
					title={$t('move_answer_down')}
					class="down"
					disabled={choiceIndex === $questions[questionIndex].choices.length - 1 || dontAnswer}
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
