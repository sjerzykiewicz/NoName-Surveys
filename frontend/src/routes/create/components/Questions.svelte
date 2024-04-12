<script lang="ts">
	import ButtonPanel from './ButtonPanel.svelte';
	import QuestionTitle from './QuestionTitle.svelte';
	import { questions } from '../stores';

	let panelVisible: boolean = false;

	function showPanel() {
		panelVisible = !panelVisible;
	}

	function handleAdd(event: CustomEvent) {
		$questions = [
			...$questions,
			{
				type: event.detail.component,
				value: ''
			}
		];
		panelVisible = !panelVisible;
	}

	function handleRemove(event: CustomEvent) {
		$questions.splice(event.detail.index, 1);
		$questions = $questions;
	}
</script>

{#each $questions as question, index}
	<QuestionTitle {index} on:removeQuestion={handleRemove} />
	<svelte:component this={question.type} />
{/each}
<button class="add-question" on:click={showPanel}>
	<i class="material-icons">add</i>Question
</button>
{#if panelVisible}
	<ButtonPanel on:addQuestion={handleAdd} />
{/if}

<style>
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
		font-size: 1.25em;
		font-weight: normal;
		font-family: 'Jura';
		color: #eaeaea;
		cursor: pointer;
		transition: background-color 0.3s;
	}

	button:hover {
		background-color: #1a1a1a;
	}

	.add-question {
		margin-right: 0.75em;
		float: left;
	}

	.material-icons {
		font-size: 0.99em;
		font-weight: bold;
		padding-right: 0.25em;
	}
</style>
