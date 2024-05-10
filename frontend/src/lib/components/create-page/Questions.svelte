<script lang="ts">
	import QuestionButtons from '$lib/components/create-page/QuestionButtons.svelte';
	import QuestionTitle from '$lib/components/create-page/QuestionTitle.svelte';
	import { QuestionError } from '$lib/entities/QuestionError';
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	function scrollToElement(selector: string) {
		const element = document.querySelector(selector) as HTMLElement;

		if (element) {
			element.scrollIntoView({ behavior: 'smooth' });
		}
	}

	function errorMessage(i: number) {
		const error = $questions[i].error;
		switch (error) {
			case QuestionError.QuestionRequired:
				return 'Please enter question no. ' + (i + 1) + '.';
			case QuestionError.ChoicesRequired:
				return 'Please enter all choices for question no. ' + (i + 1) + '.';
			case QuestionError.BinaryChoicesRequired:
				return 'Please enter both choices for question no. ' + (i + 1) + '.';
			case QuestionError.SliderValuesRequired:
				return 'Please enter both values for question no. ' + (i + 1) + '.';
			case QuestionError.DuplicateChoices:
				return 'Please remove duplicate choices from question no. ' + (i + 1) + '.';
			case QuestionError.ImproperSliderValues:
				return 'Maximum value must be greater than minimum value';
		}
	}
</script>

{#each $questions as question, questionIndex}
	<div
		class="question"
		in:slide={{ duration: 200, easing: cubicInOut }}
		on:introend={() => scrollToElement('.add-question')}
	>
		<QuestionTitle {questionIndex} />
		<svelte:component this={question.component} {questionIndex} />
	</div>
	{#key question.error}
		{#if question.error !== QuestionError.NoError}
			<p class="error">
				<i class="material-symbols-rounded">error</i>{errorMessage(questionIndex)}
			</p>
		{/if}
	{/key}
{/each}
<QuestionButtons />

<style>
	.error {
		padding-left: 2em;
		margin: -1em 0em 1em 0em;
	}

	@media screen and (max-width: 767px) {
		.error {
			font-size: 1em;
		}
	}
</style>
