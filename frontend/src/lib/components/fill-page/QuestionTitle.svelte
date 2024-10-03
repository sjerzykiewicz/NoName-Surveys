<script lang="ts">
	import { questions } from '$lib/stores/fill-page';

	export let questionIndex: number;
	export let questionTypeData: { title: string; icon: string; text: string };
</script>

<div class="question-label" id={questionIndex.toString()}>
	<div title="Question no. {questionIndex + 1}" class="index">{questionIndex + 1}.</div>
	<div title={questionTypeData.title} class="type">
		<i class="material-symbols-rounded">{questionTypeData.icon}</i>{questionTypeData.text}
	</div>
	{#if $questions[questionIndex].required}
		<div class="tooltip">
			<i class="material-symbols-rounded">asterisk</i>
			<span class="tooltip-text right">Required.</span>
		</div>
	{/if}
</div>
<div class="question-area display">
	<div class="question-title">
		{$questions[questionIndex].question}
	</div>
</div>
