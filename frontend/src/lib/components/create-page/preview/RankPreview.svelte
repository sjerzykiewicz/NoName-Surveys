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
		<label title={$t('dont_answer')} class="dont_answer">
			<div class="checkbox">
				<input
					type="checkbox"
					checked={dontAnswer}
					name="dont_answer"
					on:click={toggleDontAnswer}
				/>
				<div class="choice-input display" class:selected={dontAnswer}>
					<Tx text="dont_answer" />
				</div>
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
	.checkbox {
		padding-left: 0.9em;
		width: auto;
		display: flex;
	}
	.checkbox .choice-input {
		margin-left: 0.6em;
	}
	@media screen and (max-width: 768px) {
		.checkbox .choice-input {
			margin-left: 0.5em;
		}
	}
</style>
