<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let questionIndex: number;

	let selected: Array<boolean> = [];

	for (let i = 0; i < $questions[questionIndex].choices.length; i++) {
		selected[i] = false;
	}

	function updateAnswers(choice: string) {
		if ($answers[questionIndex].choices.includes(choice)) {
			$answers[questionIndex].choices = $answers[questionIndex].choices.filter(
				(ch) => ch !== choice
			);
		} else {
			$answers[questionIndex].choices = [...$answers[questionIndex].choices, choice];
		}
	}
</script>

<div class="choice-area display">
	{#each $questions[questionIndex].choices as choice, choiceIndex}
		<label title={$t('select_answer')} class="choice">
			<div class="checkbox">
				<input
					type="checkbox"
					on:change={() => {
						updateAnswers(choice);
						selected[choiceIndex] = !selected[choiceIndex];
					}}
				/>
			</div>
			<div class="choice-input display" class:selected={selected[choiceIndex]}>
				{choice}
			</div>
		</label>
	{/each}
</div>

<style>
	.choice {
		cursor: pointer;
	}
</style>
