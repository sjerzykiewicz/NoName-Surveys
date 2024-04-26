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
	<div class="dropdown">
		<select class="dropdown-top" disabled />
	</div>
	{#each $questions[questionIndex].choices as choice, choiceIndex}
		<div class="choice">
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
		margin-left: 2.25em;
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

	.dropdown-top {
		flex: 1;
		background-color: #4a4a4a;
		border: 1px solid #999999;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		font-size: 1.25em;
		height: 1em;
		overflow: hidden;
	}

	.dropdown-top:disabled {
		color: #eaeaea;
		opacity: 1;
	}

	.dropdown {
		display: flex;
		align-items: center;
		flex-flow: row;
		margin-bottom: 0.5em;
		margin-left: 2.25em;
		margin-right: 2.81em;
	}

	.remove-choice {
		visibility: hidden;
	}

	button {
		display: flex;
		align-items: center;
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
		.choice-input,
		.dropdown-top,
		button {
			font-size: 1em;
		}
	}
</style>
