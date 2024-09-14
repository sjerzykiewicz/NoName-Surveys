<script lang="ts">
	import { getQuestionTypeData } from '$lib/utils/getQuestionTypeData';
	import { beforeUpdate, type ComponentType } from 'svelte';

	export let question: string;
	export let questionIndex: number;
	export let questionType: ComponentType;
	export let required: boolean;

	let questionTypeData: { title: string; icon: string; text: string };

	beforeUpdate(() => {
		questionTypeData = getQuestionTypeData(questionType);
	});
</script>

<div class="question-label" id={questionIndex.toString()}>
	<div title="Question no. {questionIndex + 1}" class="index">{questionIndex + 1}.</div>
	<div title={questionTypeData.title} class="type">
		<i class="material-symbols-rounded">{questionTypeData.icon}</i>{questionTypeData.text}
	</div>
	{#if required}
		<div class="tooltip">
			<i class="material-symbols-rounded">asterisk</i>
			<span class="tooltip-text right">Required.</span>
		</div>
	{/if}
</div>
<div class="question-area display">
	<div class="question-title">
		{question}
	</div>
</div>
