<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let questionIndex: number;
	export let questionTypeData: { title: string; icon: string; text: string };
</script>

<div
	class="question-label"
	id={questionIndex.toString()}
	transition:slide={{ duration: 200, easing: cubicInOut }}
>
	<div title="{$t('question_no')} {questionIndex + 1}" class="index">{questionIndex + 1}.</div>
	<div title={$t(questionTypeData.title)} class="type">
		<i class="symbol">{questionTypeData.icon}</i><Tx text={questionTypeData.text} />
	</div>
	{#if $questions[questionIndex].required}
		<div class="tooltip">
			<i class="symbol">asterisk</i>
			<span class="tooltip-text right"><Tx text="create_question_required" /></span>
		</div>
	{/if}
</div>
<div class="question-area display" transition:slide={{ duration: 200, easing: cubicInOut }}>
	<div class="question-title">
		{$questions[questionIndex].question}
	</div>
</div>
