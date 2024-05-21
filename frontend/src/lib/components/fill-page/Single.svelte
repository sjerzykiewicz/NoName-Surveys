<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';

	export let questionIndex: number;

	let checked: number;

	function updateAnswers(choice: string, choiceIndex: number) {
		$answers[questionIndex].choices[0] = choice;
		checked = choiceIndex;
	}
</script>

<div class="choice-area">
	{#each $questions[questionIndex].choices as choice, choiceIndex}
		<label title="Select your answer" class="choice">
			<div class="radio">
				<input
					type="radio"
					name={questionIndex.toString()}
					on:change={() => {
						updateAnswers(choice, choiceIndex);
					}}
				/>
			</div>
			<div class="choice-in" class:selected={checked === choiceIndex}>
				{choice}
			</div>
		</label>
	{/each}
</div>

<style>
	.choice {
		cursor: pointer;
	}

	@media screen and (max-width: 767px) {
		.choice-area,
		.choice-in {
			font-size: 1em;
			min-width: 3em;
			min-height: 2em;
			text-align: center;
		}

		.choice-in {
			justify-content: center;
			align-items: center;
			display: flex;
			overflow-wrap: break-word;
		}
	}
</style>
