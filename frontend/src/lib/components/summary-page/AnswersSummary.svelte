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
		surveyAnswer?.questions.forEach((question, id: number) => {
			let details = '';
			let answers: (string | number)[] = [];
			let multi_answers: string[][] = [];
			let choices: string[] = [];
			let min_value = 0;
			let max_value = 0;
			switch (question?.question_type) {
				case 'text':
					details = (question as TextQuestionAnswered)?.details;
					answers = [(question as TextQuestionAnswered)?.answer];
					break;
				case 'single':
					answers = [(question as SingleQuestionAnswered)?.answer];
					choices = (question as SingleQuestionAnswered)?.choices;
					break;
				case 'multi':
					answers = (question as MultiQuestionAnswered)?.answer;
					choices = (question as MultiQuestionAnswered)?.choices;
					multi_answers = [(question as MultiQuestionAnswered)?.answer];
					break;
				case 'scale':
					answers = [(question as ScaleQuestionAnswered)?.answer];
					break;
				case 'binary':
					answers = [(question as BinaryQuestionAnswered)?.answer];
					choices = (question as BinaryQuestionAnswered)?.choices;
					break;
				case 'number':
					answers = [(question as NumberQuestionAnswered)?.answer];
					min_value = (question as NumberQuestionAnswered)?.min_value;
					max_value = (question as NumberQuestionAnswered)?.max_value;
					break;
				case 'slider':
					answers = [(question as SliderQuestionAnswered)?.answer];
					min_value = (question as SliderQuestionAnswered)?.min_value;
					max_value = (question as SliderQuestionAnswered)?.max_value;
					break;
				case 'rank':
					multi_answers = [(question as RankQuestionAnswered)?.answer];
					choices = (question as RankQuestionAnswered)?.choices;
					break;
				case 'list':
					answers = [(question as ListQuestionAnswered)?.answer];
					choices = (question as ListQuestionAnswered)?.choices;
					break;
			}

			if (groupedAnswers.length <= id) {
				groupedAnswers.push({
					required: question?.required,
					question: question?.question,
					answers: answers,
					multi_answers: multi_answers,
					question_type: question?.question_type,
					choices: choices,
					details: details,
					min_value: min_value,
					max_value: max_value
				});
			} else {
				groupedAnswers[id] = {
					required: question?.required,
					question: question?.question,
					answers: [...groupedAnswers[id].answers, ...answers],
					multi_answers: [...groupedAnswers[id].multi_answers, ...multi_answers],
					question_type: question?.question_type,
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
				<QuestionTitle
					question={question?.question}
					{questionIndex}
					questionTypeData={getQuestionTypeData(componentTypeMap[question?.question_type])}
					required={question?.required}
				/>
				<svelte:component this={componentTypeMap[question?.question_type]} data={question} />
			</div>
		{/if}
	{/each}
{/if}

<style>
	.import-export-button {
		font-size: 0.8em;
	}
</style>
