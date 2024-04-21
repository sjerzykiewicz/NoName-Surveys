<script lang="ts">
	import Single from '$lib/components/Single.svelte';
	import Multi from '$lib/components/Multi.svelte';
	import Scale from '$lib/components/Scale.svelte';
	import Slider from '$lib/components/Slider.svelte';
	import List from '$lib/components/List.svelte';
	import Rank from '$lib/components/Rank.svelte';
	import Text from '$lib/components/Text.svelte';
	import { questions } from '$lib/stores';
	import { type ComponentType } from 'svelte';
	import { slide } from 'svelte/transition';
	import { cubicInOut } from 'svelte/easing';
	import { onMount } from 'svelte';

	let isPanelVisible: boolean = false;
	let previousQuestion: ComponentType;

	function togglePanel() {
		isPanelVisible = !isPanelVisible;
	}

	function addQuestion(component: ComponentType) {
		$questions = [
			...$questions,
			{
				component: component,
				required: false,
				question: '',
				choices: []
			}
		];

		previousQuestion = component;
		isPanelVisible = false;
	}

	onMount(() => {
		function handleClick(event: MouseEvent) {
			if (isPanelVisible && !(event.target as HTMLElement).closest('.button-group')) {
				isPanelVisible = false;
			}
		}

		document.body.addEventListener('click', handleClick);

		return () => {
			document.body.removeEventListener('click', handleClick);
		};
	});
</script>

<div class="button-group" class:active={isPanelVisible}>
	<div class="add-buttons">
		<button
			class="add-question"
			class:active={isPanelVisible}
			class:previous={previousQuestion}
			on:click={togglePanel}
		>
			<i class="material-icons">add</i>Question
		</button>
		{#if previousQuestion}
			<button class="add-previous-question" on:click={() => addQuestion(previousQuestion)}>
				<i class="material-icons">repeat</i>
			</button>
		{/if}
	</div>
	{#if isPanelVisible}
		<div class="button-panel" transition:slide={{ duration: 300, easing: cubicInOut }}>
			<button class="type-button" on:click={() => addQuestion(Single)}>Single</button>
			<button class="type-button" on:click={() => addQuestion(Multi)}>Multi</button>
			<button class="type-button" on:click={() => addQuestion(Scale)}>Scale</button>
			<button class="type-button" on:click={() => addQuestion(Slider)}>Slider</button>
			<button class="type-button" on:click={() => addQuestion(List)}>List</button>
			<button class="type-button" on:click={() => addQuestion(Rank)}>Rank</button>
			<button class="last type-button" on:click={() => addQuestion(Text)}>Text</button>
		</div>
	{/if}
</div>

<style>
	button {
		background-color: #4a4a4a;
		padding: 0.25em;
		width: 6.25em;
		font-size: 1.25em;
		font-weight: normal;
		font-family: 'Jura';
		color: #eaeaea;
		cursor: pointer;
	}

	button:hover {
		background-color: #1a1a1a;
	}

	.button-group {
		width: fit-content;
		margin-bottom: 14.5em;
	}

	.button-group.active {
		margin-bottom: 0em;
		transition-delay: 0.3s;
	}

	.add-buttons {
		display: flex;
		flex-flow: row;
		justify-content: center;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
	}

	.add-question {
		display: flex;
		flex-flow: row;
		justify-content: center;
		align-items: flex-end;
		border: 1px solid #999999;
		border-radius: 5px;
		transition:
			background-color 0.3s,
			border-radius 0.3s;
	}

	.add-question.active {
		background-color: #1a1a1a;
		border-bottom-right-radius: 0px;
		border-bottom-left-radius: 0px;
	}

	.add-question.previous {
		border-top-right-radius: 0px;
		border-bottom-right-radius: 0px;
	}

	.add-previous-question {
		display: flex;
		justify-content: center;
		align-items: flex-end;
		width: 2em;
		border: 1px solid #999999;
		border-left: 0px;
		border-radius: 0px 5px 5px 0px;
		transition: background-color 0.3s;
	}

	.button-panel {
		display: flex;
		flex-flow: column;
		border-radius: 0px 0px 5px 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		width: fit-content;
		height: 14.5em;
	}

	.type-button {
		flex: 1;
		border: 0px;
		border-left: 1px solid #999999;
		border-right: 1px solid #999999;
		transition: background-color 0.3s;
	}

	.last {
		border-radius: 0px 0px 5px 5px;
		border-bottom: 1px solid #999999;
	}

	.material-icons {
		font-size: 0.99em;
		font-weight: bold;
	}

	.add-question .material-icons {
		padding-right: 0.25em;
	}
</style>
