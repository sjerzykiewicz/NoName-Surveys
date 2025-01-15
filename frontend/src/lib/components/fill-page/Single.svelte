<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let questionIndex: number;

	let checked: number;

	function updateAnswers(choice: string, choiceIndex: number) {
		if (checked === choiceIndex) {
			$answers[questionIndex].choices = [];
			checked = NaN;
		} else {
			$answers[questionIndex].choices[0] = choice;
			checked = choiceIndex;
		}
	}
</script>

<div class="choice-area display">
	{#each $questions[questionIndex].choices as choice, choiceIndex}
		<label title={$t('select_answer')} class="choice">
			<div class="checkbox">
				<input
					type="radio"
					checked={checked === choiceIndex}
					on:click={() => {
						updateAnswers(choice, choiceIndex);
					}}
				/>
			</div>
			<div class="choice-input display" class:selected={checked === choiceIndex}>
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
