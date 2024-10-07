<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { afterUpdate, tick } from 'svelte';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { handleNewLine } from '$lib/utils/handleNewLine';
	import { MOBILE_DEVICE_BREAKPOINT } from '$lib/stores/global';

	export let questionIndex: number;

	let isButtonHidden: boolean = true;
	let choiceInput: HTMLDivElement;

	async function addChoice() {
		$questions[questionIndex].choices = [...$questions[questionIndex].choices, ''];
		if (innerWidth > $MOBILE_DEVICE_BREAKPOINT) {
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

<div
	class="choice-area"
	in:slide={{ delay: 200, duration: 200, easing: cubicInOut }}
	out:slide={{ duration: 200, easing: cubicInOut }}
>
	{#each $questions[questionIndex].choices as choice, choiceIndex}
		<div class="choice">
			<div class="radio">
				<input type="radio" disabled name={questionIndex.toString()} />
			</div>
			<div
				title="Enter choice"
				class="choice-input"
				contenteditable
				bind:textContent={choice}
				bind:this={choiceInput}
				role="textbox"
				tabindex="0"
				on:keydown={handleNewLine}
			>
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
	input[type='radio'] {
		cursor: default;
	}
</style>
