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
		<button
			title="Select choice"
			class="choice"
			class:selected={selected[choiceIndex]}
			on:click={() => {
				updateAnswers(choice);
				selected[choiceIndex] = !selected[choiceIndex];
			}}
		>
			{choice}
		</button>
	{/each}
</div>

<style>
	.choice-area {
		font-size: 1em;
		font-weight: normal;
		font-family: 'Jura';
		color: #eaeaea;
		width: 86%;
	}

	.choice {
		display: flex;
		align-items: center;
		flex-flow: row;
		margin-bottom: 0.5em;
		background-color: #1a1a1a;
		color: #eaeaea;
		border: 1px solid #999999;
		font-size: 1.25em;
		border-radius: 5px;
		font-weight: normal;
		font-family: 'Jura';
		margin-left: 1.9em;
		width: 80%;
	}

	.choice.selected,
	.choice.selected:hover {
		border: 2px solid #0075ff;
	}

	@media screen and (max-width: 767px) {
		.choice {
			font-size: 1em;
		}
	}
</style>
