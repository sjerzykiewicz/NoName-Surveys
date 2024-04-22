<script lang="ts">
	import { questions } from '$lib/stores';
	import { afterUpdate } from 'svelte';

	export let questionIndex: number;

	let isButtonHidden: boolean = true;

	$questions[questionIndex].choices = ['', ''];

	function addChoice() {
		$questions[questionIndex].choices = [...$questions[questionIndex].choices, ''];
	}

	function removeChoice(index: number) {
		$questions[questionIndex].choices.splice(index, 1);
		$questions = $questions;
	}

	afterUpdate(() => {
		if ($questions[questionIndex].choices.length > 2) isButtonHidden = false;
		else isButtonHidden = true;
	});
</script>

<div class="choice-area">
	{#each $questions[questionIndex].choices as choice, choiceIndex}
		<div class="choice">
			<div class="rank">{choiceIndex + 1}.</div>
			<div class="choice-input" contenteditable bind:textContent={choice}>
				{choice}
			</div>
			<button class:remove-button={isButtonHidden} on:click={() => removeChoice(choiceIndex)}>
				<i class="material-icons">close</i>Choice
			</button>
		</div>
	{/each}
	<button class="add-choice" on:click={addChoice}>
		<i class="material-icons">add</i>Choice
	</button>
</div>

<style>
	.choice-area {
		font-size: 1em;
		font-weight: normal;
		font-family: 'Jura';
		color: #eaeaea;
		width: 85%;
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

	.remove-button {
		visibility: hidden;
	}

	.rank {
		margin-right: 0.25em;
		font-size: 1.25em;
		color: #999999;
		cursor: default;
		width: 1.5em;
		text-align: right;
	}

	button {
		display: flex;
		flex-flow: row;
		justify-content: center;
		align-items: flex-end;
		background-color: #4a4a4a;
		padding: 0.25em;
		border: 1px solid #999999;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		width: fit-content;
		font-size: 1.25em;
		font-weight: normal;
		font-family: 'Jura';
		color: #eaeaea;
		cursor: pointer;
		transition: background-color 0.3s;
	}

	button:hover {
		background-color: #1a1a1a;
	}

	.material-icons {
		font-size: 0.99em;
		font-weight: bold;
		padding-right: 0.25em;
	}
</style>
