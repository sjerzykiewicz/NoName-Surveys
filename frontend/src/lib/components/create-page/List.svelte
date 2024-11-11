<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { afterUpdate, tick } from 'svelte';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { M } from '$lib/stores/global';
	import Input from '$lib/components/global/Input.svelte';

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
	<div class="dropdown">
		<select disabled />
	</div>
	{#each $questions[questionIndex].choices as choice, choiceIndex}
		<div class="choice">
			<Input bind:text={choice} label="Choice" title="Enter a choice" bind:element={choiceInput} />
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
	.choice {
		margin-left: 2.25em;
	}

	select {
		flex: 1;
		height: 0.75em;
	}

	.dropdown {
		display: flex;
		align-items: center;
		flex-flow: row;
		margin-bottom: 0.5em;
		margin-left: 2.25em;
		margin-right: 2.25em;
	}
</style>
