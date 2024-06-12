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
	import type { ComponentType } from 'svelte';
	import type { SurveyAnswer } from '$lib/entities/surveys/SurveyAnswer';
	import type { TextQuestionAnswered } from '$lib/entities/questions/Text';
	import type { SingleQuestionAnswered } from '$lib/entities/questions/Single';
	import type { MultiQuestionAnswered } from '$lib/entities/questions/Multi';
	import type { ScaleQuestionAnswered } from '$lib/entities/questions/Scale';
	import type { BinaryQuestionAnswered } from '$lib/entities/questions/Binary';
	import type { SliderQuestionAnswered } from '$lib/entities/questions/Slider';
	import type { RankQuestionAnswered } from '$lib/entities/questions/Rank';
	import type { ListQuestionAnswered } from '$lib/entities/questions/List';

	export let surveyAnswers;

	const componentTypeMap: { [id: string]: ComponentType } = {
		text: TextSummary,
		single: SingleSummary,
		multi: MultiSummary,
		scale: ScaleSummary,
		binary: BinarySummary,
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

	surveyAnswers.forEach((surveyAnswer: SurveyAnswer) => {
		surveyAnswer.questions.forEach((question, id: number) => {
			let details = '';
			let answer: string | number = '';
			let answers: (string | number)[] = [];
			let multi_answers: string[][] = [];
			let choices: string[] = [];
			let min_value = 0;
			let max_value = 0;
			switch (question.question_type) {
				case 'text':
					details = (question as TextQuestionAnswered).details;
					answer = (question as TextQuestionAnswered).answer;
					break;
				case 'single':
					answer = (question as SingleQuestionAnswered).answer;
					choices = (question as SingleQuestionAnswered).choices;
					break;
				case 'multi':
					answers = (question as MultiQuestionAnswered).answer;
					choices = (question as MultiQuestionAnswered).choices;
					multi_answers = [(question as MultiQuestionAnswered).answer];
					break;
				case 'scale':
					answer = (question as ScaleQuestionAnswered).answer;
					break;
				case 'binary':
					answer = (question as BinaryQuestionAnswered).answer;
					choices = (question as BinaryQuestionAnswered).choices;
					break;
				case 'slider':
					answer = (question as SliderQuestionAnswered).answer;
					min_value = (question as SliderQuestionAnswered).min_value;
					max_value = (question as SliderQuestionAnswered).max_value;
					break;
				case 'rank':
					answers = (question as RankQuestionAnswered).answer;
					choices = (question as RankQuestionAnswered).choices;
					break;
				case 'list':
					answer = (question as ListQuestionAnswered).answer;
					choices = (question as ListQuestionAnswered).choices;
					break;
			}

			// this fixes the issue with indexes on text summary, but might break something else
			// if (answer != '') {
			answers = [answer];
			// }

			if (groupedAnswers.length <= id) {
				groupedAnswers.push({
					required: question.required,
					question: question.question,
					answers: answers,
					multi_answers: multi_answers,
					question_type: question.question_type,
					choices: choices,
					details: details,
					min_value: min_value,
					max_value: max_value
				});
			} else {
				groupedAnswers[id] = {
					required: question.required,
					question: question.question,
					answers: [...groupedAnswers[id].answers, ...answers],
					multi_answers: [...groupedAnswers[id].multi_answers, ...multi_answers],
					question_type: question.question_type,
					choices: choices,
					details: details,
					min_value: min_value,
					max_value: max_value
				};
			}
		});
	});
</script>

<div title="Number of answers" class="title answers">Number of answers: {surveyAnswers.length}</div>
{#each groupedAnswers as question, questionIndex}
	<div class="question">
		<QuestionTitle question={question.question} {questionIndex} required={question.required} />
		<svelte:component this={componentTypeMap[question.question_type]} data={question} />
	</div>
{/each}
