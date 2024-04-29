<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';
	export let questionIndex: number;
	let lowestChoice: number = $questions[questionIndex].choices.length - 1;

	$answers[questionIndex].choices = $questions[questionIndex].choices;

	function moveChoiceUp(choice: string) {
		let index = $answers[questionIndex].choices.findIndex((ch) => ch === choice);
		let higher = $answers[questionIndex].choices[index - 1];
		$answers[questionIndex].choices[index - 1] = choice;
		$answers[questionIndex].choices[index] = higher;
	}

	function moveChoiceDown(choice: string) {
		let index = $answers[questionIndex].choices.findIndex((ch) => ch === choice);
		let lower = $answers[questionIndex].choices[index + 1];
		$answers[questionIndex].choices[index + 1] = choice;
		$answers[questionIndex].choices[index] = lower;
	}
</script>

<div class="choice-area">
	{#each $answers[questionIndex].choices as choice, choiceIndex}
		<div class="choice">
			<div class="rank">{choiceIndex + 1}.</div>
			<div title="Enter choice" class="choice-input">
				{choice}
			</div>
			<div class="arrows">
				<button
					title="Move question up"
					class="up"
					disabled={choiceIndex === 0}
					on:click={() => moveChoiceUp(choice)}
				>
					<i class="material-symbols-rounded">arrow_drop_up</i>
				</button>
				<button
					title="Move question down"
					class="down"
					disabled={choiceIndex === lowestChoice}
					on:click={() => moveChoiceDown(choice)}
				>
					<i class="material-symbols-rounded">arrow_drop_down</i>
				</button>
			</div>
		</div>
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
	}

	.choice-input {
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

	.rank {
		margin-right: 0.25em;
		font-size: 1.25em;
		color: #999999;
		cursor: default;
		width: 1.5em;
		text-align: right;
	}

	.arrows {
		display: flex;
		flex-flow: column;
		margin-right: 0.5em;
	}

	.arrows i {
		line-height: 0.696em;
		overflow: hidden;
	}

	.up {
		border-radius: 5px 5px 0px 0px;
		border-bottom: 1px solid #999999;
		padding: 0em 0.25em 0em 0.25em;
	}

	.up:disabled {
		background-color: #1a1a1a;
		cursor: not-allowed;
	}

	.down {
		border-radius: 0px 0px 5px 5px;
		border-top: 0px;
		padding: 0em 0.25em 0em 0.25em;
	}

	.down:disabled {
		background-color: #1a1a1a;
		cursor: not-allowed;
	}

	button {
		display: flex;
		background-color: #4a4a4a;
		padding: 0.25em;
		border: 1px solid #999999;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		font-size: 1em;
		font-family: 'Jura';
		color: #eaeaea;
		cursor: pointer;
		transition: background-color 0.2s;
	}

	button:hover {
		background-color: #1a1a1a;
	}

	button:active {
		background-color: #999999;
	}

	@media screen and (max-width: 767px) {
		.choice-input {
			font-size: 1em;
		}
	}
</style>
