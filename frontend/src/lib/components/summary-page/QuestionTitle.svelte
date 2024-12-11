<script lang="ts">
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';
	import type SurveySummary from '$lib/entities/surveys/SurveySummary';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let question: string;
	export let questionIndex: number;
	export let questionTypeData: { title: string; icon: string; text: string };
	export let required: boolean;
	export let surveyStructure: SurveySummary;

	$: displayIndex =
		questionIndex +
		1 -
		surveyStructure.questions.slice(0, questionIndex).filter((q) => 'subtitle' in q).length;
</script>

<div class="question-label">
	<div title={$t('question_no', { index: displayIndex })} class="index">
		{displayIndex}.
	</div>
	<div title={$t(questionTypeData.title)} class="type">
		<i class="symbol">{questionTypeData.icon}</i><Tx text={questionTypeData.text} />
	</div>
	{#if required}
		<div class="tooltip">
			<i class="symbol">asterisk</i>
			<span class="tooltip-text right"><Tx text="question_required" /></span>
		</div>
	{/if}
</div>
<div class="question-area display">
	<div class="question-title">
		{question}
	</div>
</div>
