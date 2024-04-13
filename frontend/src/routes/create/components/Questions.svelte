<script lang="ts">
	import QuestionButtons from './QuestionButtons.svelte';
	import QuestionTitle from './QuestionTitle.svelte';
	import { questions } from '../stores';
</script>

{#each $questions as question, qIndex}
	<div class="question">
		<QuestionTitle {qIndex} />
		<svelte:component this={question.component} {qIndex} />
	</div>
{/each}
<QuestionButtons />

<style>
	.question {
		margin-bottom: 1.5em;
	}
</style>
