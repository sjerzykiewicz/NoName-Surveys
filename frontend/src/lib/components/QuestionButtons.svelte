<script lang="ts">
	import Single from '$lib/components/Single.svelte';
	import Multi from '$lib/components/Multi.svelte';
	import Scale from '$lib/components/Scale.svelte';
	import Slider from '$lib/components/Slider.svelte';
	import List from '$lib/components/List.svelte';
	import Rank from '$lib/components/Rank.svelte';
	import Text from '$lib/components/Text.svelte';
	import { questions } from '$lib/stores';
	import { type ComponentType, onMount } from 'svelte';
	import { slide } from 'svelte/transition';
	import { cubicInOut } from 'svelte/easing';

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

	function scrollToElement(selector: string) {
		const element = document.querySelector(selector) as HTMLElement;

		if (element) {
			element.scrollIntoView({ behavior: 'smooth' });
		}
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
			title="Choose question type"
			class="add-question"
			class:active={isPanelVisible}
			class:previous={previousQuestion}
			on:click={togglePanel}
		>
			<i class="material-symbols-rounded">add</i>Question
		</button>
		{#if previousQuestion}
			<button
				title="Add previous question type"
				class="add-previous-question"
				transition:slide={{ axis: 'x', duration: 300, easing: cubicInOut }}
				on:click={() => addQuestion(previousQuestion)}
			>
				<i class="material-symbols-rounded">repeat</i>
			</button>
		{/if}
	</div>
	{#if isPanelVisible}
		<div
			class="button-panel"
			transition:slide={{ duration: 300, easing: cubicInOut }}
			on:introstart={() => scrollToElement('.add-question')}
		>
			<button title="Single choice" class="type-button" on:click={() => addQuestion(Single)}
				><i class="material-symbols-rounded">radio_button_checked</i>Single</button
			>
			<button title="Multiple choice" class="type-button" on:click={() => addQuestion(Multi)}
				><i class="material-symbols-rounded">check_box</i>Multi</button
			>
			<button title="1-5 scale" class="type-button" on:click={() => addQuestion(Scale)}
				><i class="material-symbols-rounded">star</i>Scale</button
			>
			<button title="Slider" class="type-button" on:click={() => addQuestion(Slider)}
				><i class="material-symbols-rounded">sliders</i>Slider</button
			>
			<button title="Dropdown menu" class="type-button" on:click={() => addQuestion(List)}
				><i class="material-symbols-rounded">expand_circle_down</i>List</button
			>
			<button title="Ranking choice" class="type-button" on:click={() => addQuestion(Rank)}
				><i class="material-symbols-rounded">numbers</i>Rank</button
			>
			<button title="Open question" class="last type-button" on:click={() => addQuestion(Text)}
				><i class="material-symbols-rounded">text_fields</i>Text</button
			>
		</div>
	{/if}
</div>

<style>
	button {
		display: flex;
		align-items: center;
		background-color: #4a4a4a;
		padding: 0.25em;
		width: 6.25em;
		font-size: 1.25em;
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
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
	}

	.add-question {
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
		width: auto;
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

	i {
		font-size: 1.15em;
	}

	.add-question i {
		margin-right: 0.15em;
		font-variation-settings: 'wght' 900;
	}

	.type-button i {
		font-size: 1em;
		margin-right: 0.24375em;
		margin-left: 0.08125em;
	}
</style>
