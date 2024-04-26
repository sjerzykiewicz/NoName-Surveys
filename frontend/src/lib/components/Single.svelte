<script lang="ts">
	import { questions } from '$lib/stores';
	import { afterUpdate } from 'svelte';

	export let questionIndex: number;

	let isButtonHidden: boolean = true;

	function addChoice() {
		$questions[questionIndex].choices = [...$questions[questionIndex].choices, ''];
	}

	function removeChoice(index: number) {
		$questions[questionIndex].choices.splice(index, 1);
		$questions = $questions;
	}

	afterUpdate(() => {
		if ($questions[questionIndex].choices.length > 2) {
			isButtonHidden = false;
		} else {
			isButtonHidden = true;
		}
	});
</script>

<div class="choice-area">
	{#each $questions[questionIndex].choices as choice, choiceIndex}
		<div class="choice">
			<div class="radio">
				<input type="radio" disabled name={$questions[questionIndex].question} />
			</div>
			<div title="Enter choice" class="choice-input" contenteditable bind:textContent={choice}>
				{choice}
			</div>
			<button
				title="Remove choice"
				class:remove-choice={isButtonHidden}
				on:click={() => removeChoice(choiceIndex)}
			>
				<i class="material-symbols-rounded">cancel</i>
			</button>
		</div>
	{/each}
	<button title="Add choice" class="add-choice" on:click={addChoice}>
		<i class="material-symbols-rounded">add_circle</i>Choice
	</button>
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

	.choice-input[contenteditable]:empty::before {
		content: 'Enter choice...';
		color: #eaeaea40;
	}

	.remove-choice {
		visibility: hidden;
	}

	.radio {
		text-align: right;
		width: 1.75em;
		margin-right: 0.5em;
	}

	button {
		display: flex;
		background-color: #4a4a4a;
		padding: 0.25em;
		border: 1px solid #999999;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		font-size: 1.25em;
		font-family: 'Jura';
		color: #eaeaea;
		cursor: pointer;
		transition: background-color 0.2s;
	}

	button:hover {
		background-color: #1a1a1a;
	}

	.add-choice {
		margin-left: 1.8em;
	}

	i {
		font-size: 1.15em;
	}

	.add-choice i {
		margin-right: 0.15em;
	}

	@media screen and (max-width: 767px) {
		.choice-area {
			font-size: 1em;
		}

		.choice-input {
			font-size: 1em;
		}

		.add-choice i {
			font-size: 1em;
		}
	}
</style>
