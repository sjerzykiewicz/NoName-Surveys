<script lang="ts">
	import { questions } from '$lib/stores/create-page';

	export let questionIndex: number;
</script>

<div class="choice-area">
	{#each $questions[questionIndex].choices as choice}
		<div title={choice} class="choice">
			<input type="radio" disabled name={questionIndex.toString()} />
			<div class="choice-input display">
				{choice}
			</div>
		</div>
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
		text-align: center;
		margin-bottom: 0em;
	}

	.choice-input {
		background-color: var(--secondary-color);
		color: var(--text-dark-color);
		margin-top: 0.5em;
		width: 1em;
		cursor: default;
	}

	.choice-input:hover {
		background-color: var(--secondary-color);
	}

	input[type='radio'] {
		margin: 0em;
		cursor: default;
	}
</style>
