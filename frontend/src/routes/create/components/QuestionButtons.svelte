<script lang="ts">
	import Single from '../questions/Single.svelte';
	import Multi from '../questions/Multi.svelte';
	import Slider from '../questions/Slider.svelte';
	import Scale from '../questions/Scale.svelte';
	import List from '../questions/List.svelte';
	import Rank from '../questions/Rank.svelte';
	import Text from '../questions/Text.svelte';
	import { fade } from 'svelte/transition';
	import { type ComponentType } from 'svelte';
	import { questions } from '../stores';

	let panelVisible: boolean = false;

	function togglePanel() {
		panelVisible = !panelVisible;
	}

	function addQuestion(component: ComponentType) {
		$questions = [
			...$questions,
			{
				component: component,
				question: '',
				choices: []
			}
		];
		togglePanel();
	}
</script>

<button class="add-question" on:click={togglePanel}>
	<i class="material-icons">add</i>Question
</button>
{#if panelVisible}
	<div class="button-panel" transition:fade={{ duration: 200 }}>
		<button class="first type-button" on:click={() => addQuestion(Single)}>Single</button>
		<button class="type-button" on:click={() => addQuestion(Multi)}>Multi</button>
		<button class="type-button" on:click={() => addQuestion(Scale)}>Scale</button>
		<button class="type-button" on:click={() => addQuestion(Slider)}>Slider</button>
		<button class="type-button" on:click={() => addQuestion(List)}>List</button>
		<button class="type-button" on:click={() => addQuestion(Rank)}>Rank</button>
		<button class="last type-button" on:click={() => addQuestion(Text)}>Text</button>
	</div>
{/if}

<style>
	button:hover {
		background-color: #1a1a1a;
	}

	.add-question {
		display: flex;
		flex-flow: row;
		justify-content: center;
		align-items: flex-end;
		background-color: #4a4a4a;
		padding: 0.25em;
		border: 1px solid #999999;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		width: fit-content;
		font-size: 1.25em;
		font-weight: normal;
		font-family: 'Jura';
		color: #eaeaea;
		cursor: pointer;
		transition: background-color 0.3s;
		margin-right: 0.5em;
		margin-bottom: 33%;
		float: left;
	}

	.button-panel {
		display: flex;
		flex-flow: row;
		box-shadow: 0px 4px 4px #1a1a1a;
		width: fit-content;
		border-radius: 5px;
		border: 1px solid #999999;
	}

	.type-button {
		background-color: #4a4a4a;
		padding: 0.25em;
		width: fit-content;
		font-size: 1.25em;
		font-weight: normal;
		font-family: 'Jura';
		color: #eaeaea;
		border: 0px;
		cursor: pointer;
		transition: background-color 0.3s;
	}

	.first {
		border-radius: 5px 0px 0px 5px;
	}

	.last {
		border-radius: 0px 5px 5px 0px;
	}

	.material-icons {
		font-size: 0.99em;
		font-weight: bold;
		padding-right: 0.25em;
	}
</style>
