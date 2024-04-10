<script lang="ts">
	import Single from '../questions/Single.svelte';
	import Multi from '../questions/Multi.svelte';
	import Slider from '../questions/Slider.svelte';
	import Scale from '../questions/Scale.svelte';
	import List from '../questions/List.svelte';
	import Rank from '../questions/Rank.svelte';
	import Text from '../questions/Text.svelte';
	import ButtonPanel from './ButtonPanel.svelte';

	let panelVisible: boolean = false;

	function showPanel() {
		panelVisible = !panelVisible;
	}

	let questions: Array<string> = [];

	function handleQuestion(event: CustomEvent) {
		questions = [...questions, event.detail.question];
		panelVisible = !panelVisible;
	}
</script>

{#each questions as question, index}
	{#if question === 'Single'}
		<Single {index} />
	{:else if question === 'Multi'}
		<Multi {index} />
	{:else if question === 'Slider'}
		<Slider {index} />
	{:else if question === 'Scale'}
		<Scale {index} />
	{:else if question === 'List'}
		<List {index} />
	{:else if question === 'Rank'}
		<Rank {index} />
	{:else if question === 'Text'}
		<Text {index} />
	{/if}
{/each}
<button class="add-question" on:click={showPanel}>
	<i class="material-icons">add</i>Question
</button>
{#if panelVisible}
	<ButtonPanel on:addQuestion={handleQuestion} />
{/if}

<style>
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
