<script lang="ts">
	import Header from '../Header.svelte';
	import Content from '../Content.svelte';
	import Footer from '../Footer.svelte';
	import QuestionType, { questions } from './QuestionType.svelte';

	let panelVisible: boolean = false;

	function showPanel() {
		panelVisible = !panelVisible;
	}
</script>

<Header>
	<div>
		<form id="form" method="POST">
			<div class="input" contenteditable></div>
		</form>
	</div>
</Header>
<Content>
	{#each questions as question}
		<svelte:component this={question} />
	{/each}
	<button class="add-question" on:click={showPanel}>
		<i class="material-icons">add</i>Question
	</button>
	{#if panelVisible}
		<QuestionType />
	{/if}
</Content>
<Footer>
	<button class="footer-button" type="submit" form="form">
		<i class="material-icons">done</i>Save
	</button>
	<button class="footer-button">
		<i class="material-icons">remove_red_eye</i>Preview
	</button>
	<button class="footer-button">
		<i class="material-icons">arrow_back</i>Back
	</button>
</Footer>

<style>
	.input {
		background-color: #1a1a1a;
		padding: 0.25em;
		border: 1px solid #eaeaea;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		cursor: text;
		width: fit-content;
		max-width: 100%;
	}

	.input[contenteditable]:empty::before {
		content: 'Enter survey title...';
		color: #eaeaea40;
	}

	button {
		display: flex;
		flex-flow: row;
		justify-content: center;
		align-items: center;
		background-color: #4a4a4a;
		padding: 0.25em;
		border: 1px solid #eaeaea;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		width: fit-content;
		font-size: 16px;
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

	.footer-button {
		margin-left: 0.75em;
		float: right;
	}

	.material-icons {
		font-size: 16px;
		font-weight: bold;
		padding-right: 0.25em;
	}
</style>
