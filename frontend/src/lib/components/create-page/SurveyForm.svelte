<script lang="ts">
	import AddQuestionButtons from '$lib/components/create-page/AddQuestionButtons.svelte';
	import QuestionTitle from '$lib/components/create-page/QuestionTitle.svelte';
	import QuestionTitlePreview from '$lib/components/create-page/preview/QuestionTitlePreview.svelte';
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { flip } from 'svelte/animate';
	import { scrollToElement } from '$lib/utils/scrollToElement';
	import QuestionError from './QuestionError.svelte';
	import ChoiceError from './ChoiceError.svelte';

	export let isPreview: boolean;
</script>

{#each $questions as question, questionIndex (question)}
	<div
		class="question"
		in:slide={{ duration: 200, easing: cubicInOut }}
		animate:flip={{ duration: 200, easing: cubicInOut }}
		on:introend={() => scrollToElement('.add-question')}
	>
		{#if isPreview}
			<QuestionTitlePreview {questionIndex} />
			<svelte:component this={question.preview} {questionIndex} />
		{:else}
			<QuestionTitle {questionIndex} questionType={question.component} />
			<QuestionError {questionIndex} />
			<svelte:component this={question.component} {questionIndex} />
			<ChoiceError {questionIndex} />
		{/if}
	</div>
{/each}
{#if !isPreview}
	<AddQuestionButtons />
{/if}
