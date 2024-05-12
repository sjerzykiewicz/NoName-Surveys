<script lang="ts">
	import QuestionTitle from './QuestionTitle.svelte';
	import { componentTypeMap } from '$lib/utils/componentTypeMap';

	export let answer;
	export let id: string;
</script>

<div class="title">{parseFloat(id) + 1}. Answer</div>
{#each answer.questions as question, questionIndex}
	<div class="question">
		<QuestionTitle question={question.question} {questionIndex} />
		<svelte:component this={componentTypeMap[question.question_type]} data={question} />
	</div>
{/each}

<style>
	.title {
		font-size: 2em;
		margin-bottom: 1em;
	}
</style>
