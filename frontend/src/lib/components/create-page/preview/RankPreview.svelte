<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	export let questionIndex: number;

	function moveChoiceUp(index: number) {
		const higher = $questions[questionIndex].choices[index - 1];
		$questions[questionIndex].choices[index - 1] = $questions[questionIndex].choices[index];
		$questions[questionIndex].choices[index] = higher;
	}

	function moveChoiceDown(index: number) {
		const lower = $questions[questionIndex].choices[index + 1];
		$questions[questionIndex].choices[index + 1] = $questions[questionIndex].choices[index];
		$questions[questionIndex].choices[index] = lower;
	}
</script>

<div
	class="choice-area display"
	in:slide={{ duration: 200, easing: cubicInOut }}
	out:slide={{ delay: 200, duration: 200, easing: cubicInOut }}
>
	{#each $questions[questionIndex].choices as choice, choiceIndex}
		<div title="Answer no. {choiceIndex + 1}" class="choice">
			<div class="rank">{choiceIndex + 1}.</div>
			<div class="arrows">
				<button
					title="Move answer up"
					class="up"
					disabled={choiceIndex === 0}
					on:click={() => moveChoiceUp(choiceIndex)}
				>
					<i class="material-symbols-rounded">keyboard_arrow_up</i>
				</button>
				<button
					title="Move answer down"
					class="down"
					disabled={choiceIndex === $questions[questionIndex].choices.length - 1}
					on:click={() => moveChoiceDown(choiceIndex)}
				>
					<i class="material-symbols-rounded">keyboard_arrow_down</i>
				</button>
			</div>
			<div class="choice-input display">
				{choice}
			</div>
		</div>
	{/each}
</div>

<style>
	.choice-input,
	.choice-input:hover {
		background-color: var(--primary-dark-color);
		cursor: default;
	}
</style>
