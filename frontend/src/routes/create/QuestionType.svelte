<script lang="ts" context="module">
	import type { ComponentType, SvelteComponent } from 'svelte';

	export let questions: Array<ComponentType<SvelteComponent>> = [];

	function addQuestion(question: ComponentType<SvelteComponent>) {
		questions = [...questions, question];
		console.log(question);
	}
</script>

<script lang="ts">
	import Single from './Single.svelte';
	import Multi from './Multi.svelte';
	import Slider from './Slider.svelte';
	import Scale from './Scale.svelte';
	import List from './List.svelte';
	import Rank from './Rank.svelte';
	import Text from './Text.svelte';
	import { fade } from 'svelte/transition';
</script>

<div class="button-panel" transition:fade={{ duration: 300 }}>
	<button class="first" on:click={() => addQuestion(Single)}>Single</button>
	<button on:click={() => addQuestion(Multi)}>Multi</button>
	<button on:click={() => addQuestion(Slider)}>Slider</button>
	<button on:click={() => addQuestion(Scale)}>Scale</button>
	<button on:click={() => addQuestion(List)}>List</button>
	<button on:click={() => addQuestion(Rank)}>Rank</button>
	<button class="last" on:click={() => addQuestion(Text)}>Text</button>
</div>

<style>
	.button-panel {
		display: flex;
		flex-flow: row;
		box-shadow: 0px 4px 4px #1a1a1a;
		width: fit-content;
		border-radius: 5px;
	}

	button {
		background-color: #4a4a4a;
		padding: 0.25em;
		border-style: solid;
		border-width: 1px 0px 1px 0px;
		border-color: #eaeaea;
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

	.first {
		border-radius: 5px 0px 0px 5px;
		border-width: 1px 0px 1px 1px;
	}

	.last {
		border-radius: 0px 5px 5px 0px;
		border-width: 1px 1px 1px 0px;
	}
</style>
