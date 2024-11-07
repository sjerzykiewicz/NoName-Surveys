<script lang="ts">
	export let question: string;
	export let questionIndex: number;
	export let questionTypeData: { title: string; icon: string; text: string };
	export let required: boolean;
</script>

<div class="question-label" id={questionIndex.toString()}>
	<div title="Question no. {questionIndex + 1}" class="index">{questionIndex + 1}.</div>
	<div title={questionTypeData.title} class="type">
		<i class="symbol">{questionTypeData.icon}</i>{questionTypeData.text}
	</div>
	{#if required}
		<div class="tooltip">
			<i class="symbol">asterisk</i>
			<span class="tooltip-text right">Required.</span>
		</div>
	{/if}
</div>
<div class="question-area display">
	<div class="question-title">
		{question}
	</div>
</div>
