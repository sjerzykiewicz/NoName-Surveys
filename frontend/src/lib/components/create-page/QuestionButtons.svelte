<script lang="ts">
	import Single from '$lib/components/create-page/Single.svelte';
	import Multi from '$lib/components/create-page/Multi.svelte';
	import Scale from '$lib/components/create-page/Scale.svelte';
	import Slider from '$lib/components/create-page/Slider.svelte';
	import List from '$lib/components/create-page/List.svelte';
	import Rank from '$lib/components/create-page/Rank.svelte';
	import Binary from '$lib/components/create-page/Binary.svelte';
	import Text from '$lib/components/create-page/Text.svelte';
	import { questions, questionErrors } from '$lib/stores/create-page';
	import { type ComponentType, onMount } from 'svelte';
	import { slide } from 'svelte/transition';
	import { cubicInOut } from 'svelte/easing';
	import QuestionType from './QuestionType.svelte';

	let isPanelVisible: boolean = false;
	let previousQuestionType: ComponentType;
	let questionTypes: Array<ComponentType> = [
		Text,
		Single,
		Multi,
		Scale,
		Binary,
		Slider,
		Rank,
		List
	];

	function togglePanel() {
		isPanelVisible = !isPanelVisible;
	}

	function setQuestionChoices(component: ComponentType) {
		if ([Single, Multi, List, Rank].includes(component)) {
			return ['', ''];
		} else if (component === Scale) {
			return ['1', '2', '3', '4', '5'];
		} else if (component === Binary) {
			return ['Yes', 'No'];
		} else if (component === Slider) {
			return ['0', '10'];
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
		isPanelVisible = false;

		$questionErrors = [...$questionErrors, ''];
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
		{#if previousQuestionType}
			<QuestionType
				questionType={previousQuestionType}
				questionTypeIndex={-1}
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
			{#each questionTypes as questionType, questionTypeIndex}
				<QuestionType
					{questionType}
					{questionTypeIndex}
					on:addQuestionType={(event) => addQuestion(event.detail.component)}
				/>
			{/each}
		</div>
	{/if}
</div>

<style>
	button {
		width: 6.25em;
		box-shadow: none;
	}

	.button-group {
		width: fit-content;
		margin-bottom: 17em;
	}

	.add-buttons {
		display: flex;
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--shadow-color);
	}

	.add-question {
		transition:
			background-color 0.2s,
			color 0.2s,
			border-radius 0.2s;
	}

	.add-question.clicked {
		background-color: var(--accent-color);
		border-bottom-right-radius: 0px;
		border-bottom-left-radius: 0px;
		color: var(--text-color-2);
	}

	.add-question.clicked:hover {
		background-color: var(--accent-dark-color);
	}

	.add-question.clicked:active {
		background-color: var(--border-color);
	}

	.add-question.previous {
		border-top-right-radius: 0px;
		border-bottom-right-radius: 0px;
	}

	.button-panel {
		display: flex;
		flex-flow: column;
		border-radius: 0px 0px 5px 5px;
		box-shadow: 0px 4px 4px var(--shadow-color);
		width: fit-content;
		height: auto;
		position: absolute;
	}

	.add-question i {
		margin-right: 0.15em;
		font-variation-settings: 'wght' 700;
	}

	@media screen and (max-width: 767px) {
		button {
			font-size: 1em;
		}

		.button-group {
			margin-bottom: 13.5em;
		}
	}
</style>
