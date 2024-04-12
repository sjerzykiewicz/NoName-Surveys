<script lang="ts">
	import { questions } from '../stores';
	import { createEventDispatcher } from 'svelte';

	export let index: number;
	index += 1;

	const dispatch = createEventDispatcher();

	function removeQuestion() {
		dispatch('removeQuestion', { index: index - 1 });
	}
</script>

<div class="question-area">
	<div class="index">{index}.</div>
	<div class="question-input" contenteditable bind:textContent={$questions[index - 1].value}>
		{$questions[index - 1].value}
	</div>
	<button on:click={() => removeQuestion()}>
		<i class="material-icons">close</i>Question
	</button>
</div>

<style>
	.question-area {
		display: flex;
		flex-flow: row;
		align-items: center;
		margin-bottom: 0.5em;
		font-size: 1.25em;
		font-weight: normal;
		font-family: 'Jura';
		color: #eaeaea;
	}

	.question-input {
		flex: 1;
		background-color: #1a1a1a;
		padding: 0.25em;
		border: 1px solid #eaeaea;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		cursor: text;
		overflow: hidden;
		margin-right: 0.5em;
	}

	.question-input[contenteditable]:empty::before {
		content: 'Enter question...';
		color: #eaeaea40;
	}

	.index {
		margin-right: 0.25em;
		font-size: 1.25em;
		cursor: default;
	}

	button {
		display: flex;
		flex-flow: row;
		justify-content: center;
		align-items: flex-end;
		background-color: #4a4a4a;
		padding: 0.25em;
		border: 1px solid #eaeaea;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		width: fit-content;
		font-size: 1em;
		font-weight: normal;
		font-family: 'Jura';
		color: #eaeaea;
		cursor: pointer;
		transition: background-color 0.3s;
	}

	button:hover {
		background-color: #1a1a1a;
	}

	.material-icons {
		font-size: 0.99em;
		font-weight: bold;
		padding-right: 0.25em;
	}
</style>
