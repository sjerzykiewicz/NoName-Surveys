<script lang="ts">
	import { questions } from '$lib/stores/create-page';
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
	.choice {
		margin-left: 2.25em;
	}

	.dropdown-top {
		flex: 1;
		background-color: var(--primary-color);
		border: 1px solid var(--border-color);
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--box-shadow-color);
		font-size: 1.25em;
		height: 1em;
	}

	.dropdown-top:disabled {
		background-color: var(--secondary-color);
		color: var(--text-dark-color);
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

	@media screen and (max-width: 767px) {
		.choice-input,
		.dropdown-top,
		button {
			font-size: 1em;
		}

		.dropdown {
			margin-right: 2.275em;
		}

		.add-choice {
			margin-left: 2.25em;
		}
	}
</style>
