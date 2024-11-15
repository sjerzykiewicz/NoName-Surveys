<script lang="ts">
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let question: string;
	export let questionIndex: number;
	export let questionTypeData: { title: string; icon: string; text: string };
	export let required: boolean;
</script>

<div class="question-label" id={questionIndex.toString()}>
	<div title={$t('question_no', { index: questionIndex + 1 })} class="index">
		{questionIndex + 1}.
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
