<script lang="ts">
	import Single from '$lib/components/create-page/Single.svelte';
	import Multi from '$lib/components/create-page/Multi.svelte';
	import Scale from '$lib/components/create-page/Scale.svelte';
	import Slider from '$lib/components/create-page/Slider.svelte';
	import List from '$lib/components/create-page/List.svelte';
	import Rank from '$lib/components/create-page/Rank.svelte';
	import Binary from '$lib/components/create-page/Binary.svelte';
	import Text from '$lib/components/create-page/Text.svelte';
	import Number from '$lib/components/create-page/Number.svelte';
	import SinglePreview from '$lib/components/create-page/preview/SinglePreview.svelte';
	import MultiPreview from '$lib/components/create-page/preview/MultiPreview.svelte';
	import ScalePreview from '$lib/components/create-page/preview/ScalePreview.svelte';
	import SliderPreview from '$lib/components/create-page/preview/SliderPreview.svelte';
	import ListPreview from '$lib/components/create-page/preview/ListPreview.svelte';
	import RankPreview from '$lib/components/create-page/preview/RankPreview.svelte';
	import BinaryPreview from '$lib/components/create-page/preview/BinaryPreview.svelte';
	import TextPreview from '$lib/components/create-page/preview/TextPreview.svelte';
	import NumberPreview from '$lib/components/create-page/preview/NumberPreview.svelte';
	import { questions } from '$lib/stores/create-page';
	import { type ComponentType, onMount, tick } from 'svelte';
	import { slide } from 'svelte/transition';
	import { cubicInOut } from 'svelte/easing';
	import QuestionTypeButton from './QuestionTypeButton.svelte';
	import { SurveyError } from '$lib/entities/SurveyError';
	import { scrollToElement } from '$lib/utils/scrollToElement';
	import { previousQuestion } from '$lib/stores/create-page';
	import { getQuestionTypeData } from '$lib/utils/getQuestionTypeData';
	import { LIMIT_OF_CHARS } from '$lib/stores/global';
	import { M } from '$lib/stores/global';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);
	let { options } = getContext<SvelteTranslate>(CONTEXT_KEY);

	$: currentLang = $options.currentLang;

	export let questionInput: HTMLDivElement;

	let isPanelVisible: boolean = false;
	let questionTypes: Array<ComponentType> = [
		Text,
		Single,
		Multi,
		Scale,
		Binary,
		Number,
		Slider,
		List,
		Rank
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
			case Number:
				return NumberPreview;
			default:
				return TextPreview;
		}
	}

	function checkError(i: number) {
		const q = $questions[i].question;
		if (q === null || q === undefined || q.length === 0) {
			$questions[i].error = SurveyError.QuestionRequired;
		} else if (q.length > $LIMIT_OF_CHARS) {
			$questions[i].error = SurveyError.QuestionTooLong;
		} else if (
			$questions[i].component != Text &&
			$questions[i].choices.some((c) => c === null || c === undefined || c.length === 0)
		) {
			switch ($questions[i].component) {
				case Slider:
				case Number:
					$questions[i].error = SurveyError.SliderValuesRequired;
					break;
				case Binary:
					$questions[i].error = SurveyError.BinaryChoicesRequired;
					break;
				default:
					$questions[i].error = SurveyError.ChoicesRequired;
			}
		} else if ($questions[i].choices.some((c) => c.length > $LIMIT_OF_CHARS)) {
			$questions[i].error = SurveyError.ChoicesTooLong;
		} else if (
			($questions[i].component === Slider || $questions[i].component === Number) &&
			parseFloat($questions[i].choices[0]) >= parseFloat($questions[i].choices[1])
		) {
			$questions[i].error = SurveyError.ImproperSliderValues;
		} else if (new Set($questions[i].choices).size !== $questions[i].choices.length) {
			$questions[i].error = SurveyError.DuplicateChoices;
		} else {
			$questions[i].error = SurveyError.NoError;
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
			return ['0', '10', '1'];
		} else if (component === Number) {
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
				error: SurveyError.NoError
			}
		];

		$previousQuestion = component;
		isPanelVisible = false;

		if (innerWidth > $M) {
			await tick();
			questionInput.focus();
		}
	}

	onMount(() => {
		function handleEscape(event: KeyboardEvent) {
			if (isPanelVisible && event.key === 'Escape') {
				isPanelVisible = false;
				event.stopImmediatePropagation();
			}
		}

		function handleClick(event: MouseEvent) {
			if (isPanelVisible && !(event.target as HTMLElement).closest('.add-question')) {
				isPanelVisible = false;
				event.stopImmediatePropagation();
			}
		}

		document.body.addEventListener('keydown', handleEscape);
		document.body.addEventListener('click', handleClick);

		return () => {
			document.body.removeEventListener('keydown', handleEscape);
			document.body.removeEventListener('click', handleClick);
		};
	});

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

<div class="button-group" style="--width: {currentLang === 'en' ? '7.5em' : '8em'}">
	<div class="add-buttons">
		<button
			title={isPanelVisible
				? $t('create_question_choose_type_stop')
				: $t('create_question_choose_type')}
			class="add-question"
			class:clicked={isPanelVisible}
			class:previous={$previousQuestion}
			on:click={togglePanel}
		>
			<div class="button-text"><i class="symbol add">add</i><Tx text="create_question" /></div>
			<i class="symbol arrow">arrow_drop_down</i>
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
	.button-group {
		width: fit-content;
		font-size: 1.25em;
		margin-right: 0.5em;
	}

	.add-buttons {
		display: flex;
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--shadow-color-1);
	}

	.add-question {
		display: flex;
		justify-content: space-between;
		width: var(--width, 7.5em);
		box-shadow: none;
		transition:
			0.2s,
			outline 0s;
	}

	.button-text {
		display: flex;
		align-items: center;
	}

	.add-question.clicked {
		background-color: var(--primary-color-2);
		border-bottom-right-radius: 0px;
		border-bottom-left-radius: 0px;
	}

	.add-question.clicked:hover {
		background-color: var(--secondary-color-1);
	}

	.add-question.clicked:active {
		background-color: var(--border-color-1);
	}

	.add-question.previous {
		border-top-right-radius: 0px;
		border-bottom-right-radius: 0px;
	}

	.button-panel {
		display: flex;
		flex-flow: column;
		border-radius: 0px 0px 5px 5px;
		box-shadow: 0px 4px 4px var(--shadow-color-1);
		width: var(--width, 7.5em);
		height: auto;
		position: absolute;
		z-index: 1;
	}

	.add-question.clicked .add {
		transform: rotate(45deg);
	}

	.add-question.clicked .arrow {
		transform: rotate(180deg);
	}

	.add-question .add {
		margin-right: 0.15em;
		font-variation-settings: 'wght' 700;
	}

	.add-question i {
		transform: rotate(0deg);
		transition: transform 0.2s;
	}

	@media screen and (max-width: 768px) {
		.button-group {
			font-size: 1em;
		}
	}
</style>
