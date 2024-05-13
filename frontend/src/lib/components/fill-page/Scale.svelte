<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';

	export let questionIndex: number;
</script>

<div class="choice-area">
	{#each $questions[questionIndex].choices as choice}
		<label title="Select your answer" class="choice">
			<input
				type="radio"
				name={questionIndex.toString()}
				on:change={() => {
					$answers[questionIndex].choices[0] = choice;
				}}
			/>
			<div class="number" class:selected={$answers[questionIndex].choices[0] === choice}>
				{choice}
			</div>
		</label>
	{/each}
</div>

<style>
	.choice-area {
		display: flex;
		flex-flow: row;
		align-items: center;
		justify-content: space-around;
		width: calc(86% - 2.25em);
		margin-left: 2.25em;
	}

	.choice {
		flex-flow: column;
		padding: 0.5em;
		margin-bottom: 0em;
		cursor: pointer;
	}

	.number {
		font-size: 1.25em;
		margin-top: 0.25em;
		text-shadow: 0px 4px 4px var(--shadow-color);
	}

	.number.selected {
		font-weight: bold;
		color: var(--accent-color);
	}

	input[type='radio'] {
		margin: 0em;
	}

	@media screen and (max-width: 767px) {
		.choice-area,
		.number {
			font-size: 1.25em;
		}
	}
</style>
