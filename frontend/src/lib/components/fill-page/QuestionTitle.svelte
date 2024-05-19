<script lang="ts">
	import { questions } from '$lib/stores/fill-page';

	export let questionIndex: number;
</script>

<div title="Question no. {questionIndex + 1}" class="question-area display">
	<div class="index">{questionIndex + 1}.</div>
	<div class="question-title">
		{$questions[questionIndex].question}
		{#if $questions[questionIndex].required}
			<i title="Required" class="material-symbols-rounded">asterisk</i>
		{/if}
	</div>
</div>
