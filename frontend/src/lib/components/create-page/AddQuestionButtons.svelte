<script lang="ts">
	import Single from '$lib/components/create-page/Single.svelte';
	import Multi from '$lib/components/create-page/Multi.svelte';
	import Scale from '$lib/components/create-page/Scale.svelte';
	import Slider from '$lib/components/create-page/Slider.svelte';
	import List from '$lib/components/create-page/List.svelte';
	import Rank from '$lib/components/create-page/Rank.svelte';
	import Binary from '$lib/components/create-page/Binary.svelte';
	import Text from '$lib/components/create-page/Text.svelte';
	import SinglePreview from '$lib/components/create-page/preview/SinglePreview.svelte';
	import MultiPreview from '$lib/components/create-page/preview/MultiPreview.svelte';
	import ScalePreview from '$lib/components/create-page/preview/ScalePreview.svelte';
	import SliderPreview from '$lib/components/create-page/preview/SliderPreview.svelte';
	import ListPreview from '$lib/components/create-page/preview/ListPreview.svelte';
	import RankPreview from '$lib/components/create-page/preview/RankPreview.svelte';
	import BinaryPreview from '$lib/components/create-page/preview/BinaryPreview.svelte';
	import TextPreview from '$lib/components/create-page/preview/TextPreview.svelte';
	import { questions } from '$lib/stores/create-page';
	import { type ComponentType, onMount, tick } from 'svelte';
	import { slide } from 'svelte/transition';
	import { cubicInOut } from 'svelte/easing';
	import QuestionTypeButton from './QuestionTypeButton.svelte';
	import { QuestionError } from '$lib/entities/QuestionError';
	import { scrollToElement } from '$lib/utils/scrollToElement';
	import { previousQuestion } from '$lib/stores/create-page';
	import { getQuestionTypeData } from '$lib/utils/getQuestionTypeData';

	export let questionInput: HTMLDivElement;

	let isPanelVisible: boolean = false;
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

	function getPreviewComponent(component: ComponentType) {
		switch (component) {
			case Single:
				return SinglePreview;
			case Multi:
				return MultiPreview;
			case Scale:
				return ScalePreview;
			case Slider:
				return SliderPreview;
			case List:
				return ListPreview;
			case Rank:
				return RankPreview;
			case Binary:
				return BinaryPreview;
			default:
				return TextPreview;
		}
	}

	function checkError(i: number) {
		const q = $questions[i].question;
		if (q === null || q === undefined || q.length === 0) {
			$questions[i].error = QuestionError.QuestionRequired;
		} else if (
			$questions[i].component != Text &&
			$questions[i].choices.some((c) => c === null || c === undefined || c.length === 0)
		) {
			switch ($questions[i].component) {
				case Slider:
					$questions[i].error = QuestionError.SliderValuesRequired;
					break;
				case Binary:
					$questions[i].error = QuestionError.BinaryChoicesRequired;
					break;
				default:
					$questions[i].error = QuestionError.ChoicesRequired;
			}
		} else if (
			$questions[i].component === Slider &&
			parseFloat($questions[i].choices[0]) >= parseFloat($questions[i].choices[1])
		) {
			$questions[i].error = QuestionError.ImproperSliderValues;
		} else if (new Set($questions[i].choices).size !== $questions[i].choices.length) {
			$questions[i].error = QuestionError.DuplicateChoices;
		} else {
			$questions[i].error = QuestionError.NoError;
		}
	}

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

	async function addQuestion(component: ComponentType) {
		const i: number = $questions.length - 1;
		if (i >= 0) {
			checkError(i);
		}

		const choices: Array<string> = setQuestionChoices(component);

		$questions = [
			...$questions,
			{
				component: component,
				preview: getPreviewComponent(component),
				required: false,
				question: '',
				choices: choices,
				error: QuestionError.NoError
			}
		];

		$previousQuestion = component;
		isPanelVisible = false;

		await tick();
		questionInput.focus();
	}

	onMount(() => {
		function handleClick(event: MouseEvent) {
			if (isPanelVisible && !(event.target as HTMLElement).closest('.add-question')) {
				isPanelVisible = false;
			}
		}

		document.body.addEventListener('click', handleClick);

		return () => {
			document.body.removeEventListener('click', handleClick);
		};
	});
</script>

<div class="button-group">
	<div class="add-buttons">
		<button
			title={isPanelVisible ? 'Stop choosing question type' : 'Choose question type'}
			class="add-question"
			class:clicked={isPanelVisible}
			class:previous={$previousQuestion}
			on:click={togglePanel}
		>
			<i class="material-symbols-rounded">add</i>Question
		</button>
		{#if $previousQuestion}
			<QuestionTypeButton
				questionType={$previousQuestion}
				questionTypeData={getQuestionTypeData($previousQuestion)}
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
				<QuestionTypeButton
					{questionType}
					questionTypeData={getQuestionTypeData(questionType)}
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
		font-size: 1.25em;
		margin-right: 0.5em;
		margin-bottom: 0.5em;
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
		z-index: 100;
	}

	.add-question.clicked i {
		transform: rotate(45deg);
	}

	.add-question i {
		margin-right: 0.15em;
		font-variation-settings: 'wght' 700;
		transform: rotate(0deg);
		transition: transform 0.2s;
	}

	@media screen and (max-width: 767px) {
		.button-group {
			font-size: 1em;
		}
	}
</style>
