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
		<label class="choice-div">
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
			<div title="Enter choice" class="choice" class:selected={selected[choiceIndex]}>
				{choice}
			</div>
		</label>
	{/each}
</div>

<style>
	input[type='checkbox']:checked {
		accent-color: #0075ff;
	}

	.choice-area {
		font-size: 1em;
		font-weight: normal;
		font-family: 'Jura';
		color: #eaeaea;
		width: 86%;
	}

	.choice-div {
		display: flex;
		align-items: center;
		flex-flow: row;
		margin-bottom: 0.5em;
	}

	.choice {
		flex: 1;
		background-color: #1a1a1a;
		padding: 0.25em;
		border: 1px solid #999999;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		font-size: 1.25em;
		cursor: text;
		overflow: hidden;
		margin-right: 0.5em;
	}

	.choice.selected,
	.choice.selected:hover {
		border: 2px solid #0075ff;
	}

	.radio {
		text-align: right;
		width: 1.75em;
		margin-right: 0.5em;
	}

	@media screen and (max-width: 767px) {
		.choice-area,
		.choice {
			font-size: 1em;
		}
	}
</style>
