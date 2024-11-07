<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { afterUpdate, tick } from 'svelte';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { handleNewLine } from '$lib/utils/handleNewLine';
	import { LIMIT_OF_CHARS } from '$lib/stores/global';
	import { limitInput } from '$lib/utils/limitInput';
	import { M } from '$lib/stores/global';

	export let questionIndex: number;

	let isButtonHidden: boolean = true;
	let choiceInput: HTMLDivElement;

	async function addChoice() {
		$questions[questionIndex].choices = [...$questions[questionIndex].choices, ''];
		if (innerWidth > $M) {
			await tick();
			choiceInput.focus();
		}
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

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

<div class="choice-area" transition:slide={{ duration: 200, easing: cubicInOut }}>
	{#each $questions[questionIndex].choices as choice, choiceIndex}
		<div class="choice">
			<div class="radio">
				<input type="radio" disabled name={questionIndex.toString()} />
			</div>
			<div class="input-container" class:max={choice.length > $LIMIT_OF_CHARS}>
				<div
					title="Enter choice"
					class="choice-input"
					contenteditable
					bind:textContent={choice}
					bind:this={choiceInput}
					role="textbox"
					tabindex="0"
					on:keydown={(e) => {
						handleNewLine(e);
						limitInput(e, choice, $LIMIT_OF_CHARS);
					}}
				>
					{choice}
				</div>
				<span class="char-count">{choice.length} / {$LIMIT_OF_CHARS}</span>
			</div>
			<button
				title="Remove choice"
				class="remove-choice"
				class:hidden={isButtonHidden}
				on:click={() => removeChoice(choiceIndex)}
			>
				<i class="symbol">delete</i>
			</button>
		</div>
	{/each}
	<button title="Add choice" class="add-choice" on:click={addChoice}>
		<i class="symbol">add</i>Choice
	</button>
</div>

<style>
	input[type='radio'] {
		cursor: default;
	}
</style>
