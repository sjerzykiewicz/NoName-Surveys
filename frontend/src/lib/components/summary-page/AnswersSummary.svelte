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

	export let answers;

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
		question_type: string;
		choices: string[];
		details: string;
		min_value: number;
		max_value: number;
	}[] = [];

	answers.forEach((answer) => {
		answer.questions.forEach((question, id) => {
			if (groupedAnswers.length <= id) {
				groupedAnswers.push({
					required: question.required,
					question: question.question,
					answers: [question.answer],
					question_type: question.question_type,
					choices: question.choices,
					details: question.details,
					min_value: question.min_value,
					max_value: question.max_value
				});
			} else {
				groupedAnswers[id] = {
					required: question.required,
					question: question.question,
					answers: [...groupedAnswers[id].answers, question.answer],
					question_type: question.question_type,
					choices: question.choices,
					details: question.details,
					min_value: question.min_value,
					max_value: question.max_value
				};
			}
		});
	});
</script>

{#each groupedAnswers as question, questionIndex}
	<div class="question">
		<QuestionTitle question={question.question} {questionIndex} />
		<svelte:component this={componentTypeMap[question.question_type]} data={question} />
	</div>
{/each}

<style>
</style>
