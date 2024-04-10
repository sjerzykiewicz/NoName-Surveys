<script lang="ts">
	import { fade } from 'svelte/transition';
	import { createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();

	function addQuestion(type: string) {
		dispatch('addQuestion', { question: type });
	}
</script>

<div class="button-panel" transition:fade={{ duration: 200 }}>
	<button class="first" on:click={() => addQuestion('Single')}>Single</button>
	<button on:click={() => addQuestion('Multi')}>Multi</button>
	<button on:click={() => addQuestion('Slider')}>Slider</button>
	<button on:click={() => addQuestion('Scale')}>Scale</button>
	<button on:click={() => addQuestion('List')}>List</button>
	<button on:click={() => addQuestion('Rank')}>Rank</button>
	<button class="last" on:click={() => addQuestion('Text')}>Text</button>
</div>

<style>
	.button-panel {
		display: flex;
		flex-flow: row;
		box-shadow: 0px 4px 4px #1a1a1a;
		width: fit-content;
		border-radius: 5px;
		border: 1px solid #eaeaea;
	}

	button {
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

	button:hover {
		background-color: #1a1a1a;
	}

	.first {
		border-radius: 5px 0px 0px 5px;
	}

	.last {
		border-radius: 0px 5px 5px 0px;
	}
</style>
