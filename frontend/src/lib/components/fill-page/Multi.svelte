<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';

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

<div class="choice-area">
	{#each $questions[questionIndex].choices as choice, choiceIndex}
		<label title="Select your answer" class="choice">
			<div class="radio">
				<input
					type="checkbox"
					name={$questions[questionIndex].question}
					on:click={() => {
						updateAnswers(choice);
						selected[choiceIndex] = !selected[choiceIndex];
					}}
				/>
			</div>
			<div class="choice-in" class:selected={selected[choiceIndex]}>
				{choice}
			</div>
		</label>
	{/each}
</div>

<style>
	.choice {
		width: fit-content;
		cursor: pointer;
	}

	@media screen and (max-width: 767px) {
		.choice-area,
		.choice-in {
			font-size: 1em;
		}
	}
</style>
