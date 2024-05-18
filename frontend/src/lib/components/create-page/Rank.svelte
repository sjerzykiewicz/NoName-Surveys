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
			<div class="rank">{choiceIndex + 1}.</div>
			<div title="Enter choice" class="choice-input" contenteditable bind:textContent={choice}>
				{choice}
			</div>
			<button
				title="Remove choice"
				class="remove-choice"
				class:hidden={isButtonHidden}
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
	.rank {
		color: var(--border-color);
		cursor: default;
	}
</style>
