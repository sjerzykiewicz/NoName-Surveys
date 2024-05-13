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

	.arrows i {
		font-variation-settings: 'wght' 700;
	}

	button {
		font-size: 1em;
	}

	@media screen and (max-width: 767px) {
		.choice-in,
		.arrows,
		.rank {
			font-size: 1.2em;
		}

		.arrows {
			font-size: 1.5em;
		}

		.choice {
			max-width: 100%;
		}

		.choice-in {
			overflow-wrap: break-word;
		}

		.rank {
			width: 2em;
			margin-left: -0.5em;
		}
	}
</style>
