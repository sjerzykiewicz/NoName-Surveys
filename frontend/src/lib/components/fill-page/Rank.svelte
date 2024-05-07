<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';

	export let questionIndex: number;

	$answers[questionIndex].choices = $questions[questionIndex].choices;

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
</script>

<div class="choice-area">
	{#each $answers[questionIndex].choices as choice, choiceIndex}
		<div class="choice">
			<div class="rank">{choiceIndex + 1}.</div>
			<div class="arrows">
				<button
					title="Move answer up"
					class="up"
					disabled={choiceIndex === 0}
					on:click={() => moveChoiceUp(choiceIndex)}
				>
					<i class="material-symbols-rounded">arrow_drop_up</i>
				</button>
				<button
					title="Move answer down"
					class="down"
					disabled={choiceIndex === $questions[questionIndex].choices.length - 1}
					on:click={() => moveChoiceDown(choiceIndex)}
				>
					<i class="material-symbols-rounded">arrow_drop_down</i>
				</button>
			</div>
			<div class="choice-in">
				{choice}
			</div>
		</div>
	{/each}
</div>

<style>
	.choice {
		width: fit-content;
	}

	.choice-in {
		cursor: default;
	}

	.choice-in:hover {
		background-color: var(--primary-color);
	}

	.rank {
		margin-right: 0.25em;
		font-size: 1.25em;
		color: var(--text-color);
		cursor: default;
		width: 1.5em;
		text-align: right;
	}

	.arrows {
		font-size: 1.25em;
	}

	.up {
		border-radius: 5px 5px 0px 0px;
		border-bottom: 1px solid var(--border-color);
		padding: 0em 0.25em 0em 0.25em;
	}

	.up:disabled {
		background-color: var(--secondary-color);
		cursor: not-allowed;
	}

	.down {
		border-radius: 0px 0px 5px 5px;
		border-top: 0px;
		padding: 0em 0.25em 0em 0.25em;
	}

	.down:disabled {
		background-color: var(--secondary-color);
		cursor: not-allowed;
	}

	button {
		display: flex;
		background-color: var(--primary-color);
		padding: 0.25em;
		border: 1px solid var(--border-color);
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--box-shadow-color);
		font-size: 1em;
		color: var(--text-color);
		cursor: pointer;
		transition: background-color 0.2s;
	}

	button:hover {
		background-color: var(--secondary-color);
	}

	button:active {
		background-color: var(--border-color);
	}

	@media screen and (max-width: 767px) {
		.choice-in,
		.arrows,
		.rank {
			font-size: 1em;
		}

		.rank {
			width: 2em;
		}
	}
</style>
