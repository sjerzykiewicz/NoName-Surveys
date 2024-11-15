<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);
	export let questionIndex: number;

	function moveChoiceUp(index: number) {
		const higher = $questions[questionIndex].choices[index - 1];
		$questions[questionIndex].choices[index - 1] = $questions[questionIndex].choices[index];
		$questions[questionIndex].choices[index] = higher;
	}

	function moveChoiceDown(index: number) {
		const lower = $questions[questionIndex].choices[index + 1];
		$questions[questionIndex].choices[index + 1] = $questions[questionIndex].choices[index];
		$questions[questionIndex].choices[index] = lower;
	}
</script>

<div class="choice-area display" transition:slide={{ duration: 200, easing: cubicInOut }}>
	{#each $questions[questionIndex].choices as choice, choiceIndex}
		<div title="Answer no. {choiceIndex + 1}" class="choice">
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
					disabled={choiceIndex === $questions[questionIndex].choices.length - 1}
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
</div>

<style>
	.choice-input,
	.choice-input:hover {
		background-color: var(--primary-color-2);
		cursor: default;
	}
</style>
