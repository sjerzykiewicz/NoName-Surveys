<script lang="ts">
	import QuestionButtons from '$lib/components/QuestionButtons.svelte';
	import QuestionTitle from '$lib/components/QuestionTitle.svelte';
	import { questions } from '$lib/stores';
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
		margin-bottom: 2em;
	}
</style>
