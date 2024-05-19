<script lang="ts">
	export let question: string;
	export let questionIndex: number;
	export let required: boolean;
</script>

<div title="Question no. {questionIndex + 1}" class="question-area display">
	<div class="index">{questionIndex + 1}.</div>
	<div class="question-title">
		{question}
		{#if required}
			<i title="Required" class="material-symbols-rounded">asterisk</i>
		{/if}
	</div>
</div>
