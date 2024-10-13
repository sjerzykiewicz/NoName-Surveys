<script lang="ts">
	import QuestionTitle from '../QuestionTitle.svelte';
	import Single from './Single.svelte';
	import Text from './Text.svelte';
	import List from './List.svelte';
	import Scale from './Scale.svelte';
	import Multi from './Multi.svelte';
	import Slider from './Slider.svelte';
	import Binary from './Binary.svelte';
	import Rank from './Rank.svelte';
	import Number from './Number.svelte';
	import type { ComponentType } from 'svelte';
	import { getQuestionTypeData } from '$lib/utils/getQuestionTypeData';

	export let answer;
	export let id: string;

	export const componentTypeMap: { [id: string]: ComponentType } = {
		text: Text,
		single: Single,
		multi: Multi,
		scale: Scale,
		binary: Binary,
		number: Number,
		slider: Slider,
		rank: Rank,
		list: List
	};
</script>

<div title="Answer no. {parseFloat(id) + 1}" class="title answers">
	{parseFloat(id) + 1}. Answer
</div>
{#each answer.questions as question, questionIndex}
	<div class="question">
		<QuestionTitle
			question={question.question}
			{questionIndex}
			questionTypeData={getQuestionTypeData(componentTypeMap[question.question_type])}
			required={question.required}
		/>
		<svelte:component this={componentTypeMap[question.question_type]} data={question} />
	</div>
{/each}
