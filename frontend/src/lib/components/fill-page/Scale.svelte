<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';

	export let questionIndex: number;
</script>

<div class="choice-area display">
	{#each $questions[questionIndex].choices as choice}
		<label title="Select your answer" class="choice">
			<input
				type="radio"
				name={questionIndex.toString()}
				on:change={() => {
					$answers[questionIndex].choices[0] = choice;
				}}
			/>
			<div
				class="choice-input display"
				class:selected={$answers[questionIndex].choices[0] === choice}
			>
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
		width: calc(100% - 4.5em);
		margin-left: 2.25em;
	}

	.choice {
		flex-flow: column;
		text-align: center;
		margin-bottom: 0em;
		padding: 0.5em;
		cursor: pointer;
	}

	.choice-input {
		margin-top: 0.5em;
		width: 1em;
	}

	input[type='radio'] {
		margin: 0em;
	}

	@media screen and (max-width: 767px) {
		.choice-area,
		.choice-input {
			font-size: 1em;
		}
	}
</style>
