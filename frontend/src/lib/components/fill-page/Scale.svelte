<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';
	export let questionIndex: number;

	let selected: number;

	function handleClick(id: number, choice: string) {
		if (selected !== id) {
			selected = id;
			$answers[questionIndex].choices[0] = choice;
		}
	}
</script>

<div class="choice-area">
	{#each $questions[questionIndex].choices as choice, choiceIndex}
		<button
			title="Select choice"
			class="choice number"
			class:selected={selected === choiceIndex}
			on:click={() => handleClick(choiceIndex, choice)}
		>
			{choice}
		</button>
	{/each}
</div>

<style>
	.choice-area {
		display: flex;
		flex-flow: row;
		align-items: center;
		justify-content: space-around;
		font-size: 1em;
		font-weight: normal;
		font-family: 'Jura';
		color: #eaeaea;
		width: calc(86% - 2.25em);
		margin-left: 2.25em;
	}

	.choice {
		display: flex;
		align-items: center;
		flex-flow: row;
		margin-bottom: 0.5em;
		background-color: #1a1a1a;
		color: #eaeaea;
		border: 1px solid #999999;
		font-size: 1.25em;
		border-radius: 5px;
		font-weight: normal;
		font-family: 'Jura';
		margin-left: 1.9em;
		padding: 1px;
		width: 4%;
		align-items: center;
		justify-content: center;
	}

	.choice.selected,
	.choice.selected:hover {
		border: 2px solid #0075ff;
	}

	.number {
		font-size: 1.25em;
		cursor: default;
	}

	@media screen and (max-width: 767px) {
		.choice-area,
		.number {
			font-size: 1em;
		}
	}
</style>
