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
				class="create-page-button"
				class:remove-choice={isButtonHidden}
				on:click={() => removeChoice(choiceIndex)}
			>
				<i class="material-symbols-rounded">cancel</i>
			</button>
		</div>
	{/each}
	<button title="Add choice" class="create-page-button add-choice" on:click={addChoice}>
		<i class="material-symbols-rounded">add_circle</i>Choice
	</button>
</div>

<style>
	.radio {
		text-align: right;
		width: 1.75em;
		margin-right: 0.5em;
	}

	@media screen and (max-width: 767px) {
		.choice-area,
		.choice-input,
		button {
			font-size: 1em;
		}
	}
</style>
