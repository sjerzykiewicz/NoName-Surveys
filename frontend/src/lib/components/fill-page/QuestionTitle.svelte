<script lang="ts">
	import { questions } from '$lib/stores/fill-page';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let questionIndex: number;
	export let questionTypeData: { title: string; icon: string; text: string };

	$: displayIndex =
		questionIndex +
		1 -
		$questions.slice(0, questionIndex).filter((q) => q.type === 'subtitle').length;
</script>

<div class="question-label">
	<div title={$t('question_no', { index: displayIndex })} class="index">
		{displayIndex}.
	</div>
	<div title={$t(questionTypeData.title)} class="type">
		<i class="symbol">{questionTypeData.icon}</i><Tx text={questionTypeData.text} />
	</div>
	{#if $questions[questionIndex].required}
		<div class="tooltip">
			<i class="symbol">asterisk</i>
			<span class="tooltip-text right"><Tx text="question_required" /></span>
		</div>
	{/if}
</div>
<div class="question-area display">
	<div class="question-title">
		{$questions[questionIndex].question}
	</div>
</div>
