<script lang="ts">
	import QuestionButtons from '$lib/components/QuestionButtons.svelte';
	import QuestionTitle from '$lib/components/QuestionTitle.svelte';
	import { questions } from '$lib/stores';
</script>

{#each $questions as question, questionIndex}
	<div class="question">
		<QuestionTitle {questionIndex} />
		<svelte:component this={question.component} {questionIndex} />
	</div>
{/each}
<QuestionButtons />

<style>
	.question {
		margin-bottom: 2em;
	}
</style>
