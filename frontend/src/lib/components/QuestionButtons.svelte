<script lang="ts">
	import Single from '$lib/components/Single.svelte';
	import Multi from '$lib/components/Multi.svelte';
	import Scale from '$lib/components/Scale.svelte';
	import Slider from '$lib/components/Slider.svelte';
	import List from '$lib/components/List.svelte';
	import Rank from '$lib/components/Rank.svelte';
	import YesNo from '$lib/components/YesNo.svelte';
	import Text from '$lib/components/Text.svelte';
	import { questions } from '$lib/stores';
	import { type ComponentType, onMount } from 'svelte';
	import { slide } from 'svelte/transition';
	import { cubicInOut } from 'svelte/easing';
	import QuestionType from './QuestionType.svelte';

	let isPanelVisible: boolean = false;
	let isQuestionAdded: boolean = false;
	let previousQuestionType: ComponentType;
	let questionTypes: Array<ComponentType> = [Text, Single, Multi, Scale, YesNo, Slider, Rank, List];

	function togglePanel() {
		isPanelVisible = !isPanelVisible;
	}

	function setQuestionChoices(component: ComponentType) {
		if ([Single, Multi, Slider, List, Rank].includes(component)) {
			return ['', ''];
		} else if (component === Scale) {
			return ['1', '2', '3', '4', '5'];
		} else if (component === YesNo) {
			return ['Yes', 'No'];
		} else {
			return [''];
		}
	}

	function addQuestion(component: ComponentType) {
		const choices: Array<string> = setQuestionChoices(component);

		$questions = [
			...$questions,
			{
				component: component,
				required: false,
				question: '',
				choices: choices
			}
		];

		previousQuestionType = component;
		isQuestionAdded = true;
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

<div class="button-group" class:clicked={isPanelVisible} class:previous={previousQuestionType}>
	<div class="add-buttons">
		<button
			title="Choose question type"
			class="add-question"
			class:clicked={isPanelVisible}
			class:previous={previousQuestionType}
			on:click={togglePanel}
		>
			<i class="material-symbols-rounded">add</i>Question
		</button>
		{#if isQuestionAdded}
			<QuestionType
				questionType={previousQuestionType}
				questionTypeIndex={-1}
				{isQuestionAdded}
				on:addQuestionType={(event) => addQuestion(event.detail.component)}
			/>
		{/if}
	</div>
	{#if isPanelVisible}
		<div
			class="button-panel"
			transition:slide={{ duration: 200, easing: cubicInOut }}
			on:introstart={() => scrollToElement('.add-question')}
		>
			{#each questionTypes.filter((questionType) => questionType !== previousQuestionType) as questionType, questionTypeIndex}
				<QuestionType
					{questionType}
					{questionTypeIndex}
					{isQuestionAdded}
					on:addQuestionType={(event) => addQuestion(event.detail.component)}
				/>
			{/each}
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

	button:active {
		background-color: #999999;
	}

	.button-group {
		width: fit-content;
		margin-bottom: 16.57em;
	}

	.button-group.clicked {
		margin-bottom: 0em;
		transition-delay: 0.2s;
	}

	.button-group.previous {
		margin-bottom: 14.5em;
	}

	.button-group.clicked.previous {
		margin-bottom: 0em;
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
			background-color 0.2s,
			border-radius 0.2s;
	}

	.add-question.clicked {
		background-color: #0075ff;
		border-bottom-right-radius: 0px;
		border-bottom-left-radius: 0px;
	}

	.add-question.clicked:hover {
		background-color: #001c53;
	}

	.add-question.clicked:active {
		background-color: #999999;
	}

	.add-question.previous {
		border-top-right-radius: 0px;
		border-bottom-right-radius: 0px;
	}

	.button-panel {
		display: flex;
		flex-flow: column;
		border-radius: 0px 0px 5px 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		width: fit-content;
		height: auto;
	}

	i {
		font-size: 1.15em;
	}

	.add-question i {
		margin-right: 0.15em;
		font-variation-settings: 'wght' 700;
	}
</style>
