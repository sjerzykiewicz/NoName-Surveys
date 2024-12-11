<script lang="ts">
	import QuestionTitle from './QuestionTitle.svelte';
	import SingleSummary from '$lib/components/summary-page/SingleSummary.svelte';
	import TextSummary from '$lib/components/summary-page/TextSummary.svelte';
	import ListSummary from '$lib/components/summary-page/ListSummary.svelte';
	import ScaleSummary from '$lib/components/summary-page/ScaleSummary.svelte';
	import MultiSummary from '$lib/components/summary-page/MultiSummary.svelte';
	import SliderSummary from '$lib/components/summary-page/SliderSummary.svelte';
	import BinarySummary from '$lib/components/summary-page/BinarySummary.svelte';
	import RankSummary from '$lib/components/summary-page/RankSummary.svelte';
	import NumberSummary from '$lib/components/summary-page/NumberSummary.svelte';
	import type { ComponentType } from 'svelte';
	import type { TextQuestionAnswered } from '$lib/entities/questions/Text';
	import type { SingleQuestionAnswered } from '$lib/entities/questions/Single';
	import type { MultiQuestionAnswered } from '$lib/entities/questions/Multi';
	import type { ScaleQuestionAnswered } from '$lib/entities/questions/Scale';
	import type { BinaryQuestionAnswered } from '$lib/entities/questions/Binary';
	import type { SliderQuestionAnswered } from '$lib/entities/questions/Slider';
	import type { RankQuestionAnswered } from '$lib/entities/questions/Rank';
	import type { ListQuestionAnswered } from '$lib/entities/questions/List';
	import type { NumberQuestionAnswered } from '$lib/entities/questions/Number';
	import SurveySummary from '$lib/entities/surveys/SurveySummary';
	import { getQuestionTypeData } from '$lib/utils/getQuestionTypeData';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';
	import { downloadFile } from '$lib/utils/downloadFile';
	import SubtitleComponent from './Subtitle.svelte';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let surveyAnswers: Array<SurveySummary>;
	export let isImported: boolean = false;

	const componentTypeMap: { [id: string]: ComponentType } = {
		text: TextSummary,
		single: SingleSummary,
		multi: MultiSummary,
		scale: ScaleSummary,
		binary: BinarySummary,
		number: NumberSummary,
		slider: SliderSummary,
		rank: RankSummary,
		list: ListSummary
	};

	let groupedAnswers: {
		required: boolean;
		question: string;
		answers: (string | number)[];
		multi_answers: string[][];
		question_type: string;
		choices: string[];
		details: string;
		min_value: number;
		max_value: number;
	}[] = [];

	surveyAnswers.forEach((surveyAnswer) => {
		surveyAnswer?.questions.forEach((q, id: number) => {
			let required: boolean = false;
			let question: string = '';
			let question_type: string = '';
			let details: string = '';
			let answers: (string | number)[] = [];
			let multi_answers: string[][] = [];
			let choices: string[] = [];
			let min_value: number = 0;
			let max_value: number = 0;
			if ('subtitle' in q) {
				required = false;
				question = q?.subtitle;
				question_type = 'subtitle';
			} else {
				required = q?.required;
				question = q?.question;
				question_type = q?.question_type;
				switch (q?.question_type) {
					case 'text':
						details = (q as TextQuestionAnswered)?.details;
						answers = [(q as TextQuestionAnswered)?.answer];
						break;
					case 'single':
						answers = [(q as SingleQuestionAnswered)?.answer];
						choices = (q as SingleQuestionAnswered)?.choices;
						break;
					case 'multi':
						answers = (q as MultiQuestionAnswered)?.answer;
						choices = (q as MultiQuestionAnswered)?.choices;
						multi_answers = [(q as MultiQuestionAnswered)?.answer];
						break;
					case 'scale':
						answers = [(q as ScaleQuestionAnswered)?.answer];
						break;
					case 'binary':
						answers = [(q as BinaryQuestionAnswered)?.answer];
						choices = (q as BinaryQuestionAnswered)?.choices;
						break;
					case 'number':
						answers = [(q as NumberQuestionAnswered)?.answer];
						min_value = (q as NumberQuestionAnswered)?.min_value;
						max_value = (q as NumberQuestionAnswered)?.max_value;
						break;
					case 'slider':
						answers = [(q as SliderQuestionAnswered)?.answer];
						min_value = (q as SliderQuestionAnswered)?.min_value;
						max_value = (q as SliderQuestionAnswered)?.max_value;
						break;
					case 'rank':
						multi_answers = [(q as RankQuestionAnswered)?.answer];
						choices = (q as RankQuestionAnswered)?.choices;
						break;
					case 'list':
						answers = [(q as ListQuestionAnswered)?.answer];
						choices = (q as ListQuestionAnswered)?.choices;
						break;
				}
			}

			if (groupedAnswers.length <= id) {
				groupedAnswers.push({
					required: required,
					question: question,
					answers: answers,
					multi_answers: multi_answers,
					question_type: question_type,
					choices: choices,
					details: details,
					min_value: min_value,
					max_value: max_value
				});
			} else {
				groupedAnswers[id] = {
					required: required,
					question: question,
					answers: [...groupedAnswers[id].answers, ...answers],
					multi_answers: [...groupedAnswers[id].multi_answers, ...multi_answers],
					question_type: question_type,
					choices: choices,
					details: details,
					min_value: min_value,
					max_value: max_value
				};
			}
		});
	});
</script>

{#if surveyAnswers.length === 0}
	<div title={$t('number_of_answers_title')} class="title empty"><Tx text="no_answers_yet" /></div>
{:else}
	<div title={$t('number_of_answers_title')} class="title answers static">
		<Tx text="number_of_answers" params={{ number: surveyAnswers.length }} />
		{#if !isImported}
			<button
				title={$t('export_survey_summary')}
				class="import-export-button"
				on:click={() =>
					downloadFile(
						`${surveyAnswers[0].title}.json`,
						'application/json',
						JSON.stringify(surveyAnswers)
					)}><i class="symbol">file_save</i><Tx text="export" /></button
			>
		{/if}
	</div>
	{#each groupedAnswers as question, questionIndex}
		{#if question?.question && question?.question_type && typeof question?.required === 'boolean'}
			<div class="question">
				{#if question.question_type === 'subtitle'}
					<SubtitleComponent question={question.question} />
				{:else}
					<QuestionTitle
						question={question.question}
						{questionIndex}
						questionTypeData={getQuestionTypeData(componentTypeMap[question.question_type])}
						required={question.required}
						surveyStructure={surveyAnswers[0]}
					/>
					<svelte:component this={componentTypeMap[question.question_type]} data={question} />
				{/if}
			</div>
		{/if}
	{/each}
{/if}

<style>
	.import-export-button {
		font-size: 0.8em;
	}
</style>
