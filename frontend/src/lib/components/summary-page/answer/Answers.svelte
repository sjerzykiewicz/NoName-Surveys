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
	import Subtitle from '../Subtitle.svelte';
	import type { ComponentType } from 'svelte';
	import { getQuestionTypeData } from '$lib/utils/getQuestionTypeData';
	import type SurveySummary from '$lib/entities/surveys/SurveySummary';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);
	export let answer: SurveySummary;
	export let id: number;

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

<div title={$t('answer_no', { index: id + 1 })} class="title answers">
	{id + 1}. <Tx text="answer" />
</div>
{#each answer.questions as question, questionIndex}
	<div class="question">
		{#if 'subtitle' in question}
			<Subtitle question={question.subtitle} />
		{:else}
			<div class="question">
				<QuestionTitle
					question={question.question}
					{questionIndex}
					questionTypeData={getQuestionTypeData(componentTypeMap[question.question_type])}
					required={question.required}
					surveyStructure={answer}
				/>
				<svelte:component this={componentTypeMap[question.question_type]} data={question} />
			</div>
		{/if}
	</div>
{/each}
