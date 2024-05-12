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
				return 'Maximum value must be greater than minimum value in question no. ' + (i + 1) + '.';
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

		{#key question.error}
			{#if question.error === QuestionError.QuestionRequired && !question.question}
				<p title="Error" class="error question-error">
					<i class="material-symbols-rounded">error</i>{errorMessage(questionIndex)}
				</p>
			{/if}

			<svelte:component this={question.component} {questionIndex} />

			{#if ([QuestionError.ChoicesRequired, QuestionError.BinaryChoicesRequired, QuestionError.SliderValuesRequired].includes(question.error) && question.choices.some((c) => !c)) || (question.error === QuestionError.DuplicateChoices && new Set(question.choices).size !== question.choices.length) || (question.error === QuestionError.ImproperSliderValues && parseFloat(question.choices[0]) >= parseFloat(question.choices[1]))}
				<p title="Error" class="error choice-error">
					<i class="material-symbols-rounded">error</i>{errorMessage(questionIndex)}
				</p>
			{/if}
		{/key}
	</div>
{/each}
<QuestionButtons />

<style>
	.error {
		padding-left: 2em;
	}

	.question-error {
		margin-top: -0.5em;
		margin-bottom: 0.5em;
	}

	.choice-error {
		margin-top: 0.5em;
	}

	@media screen and (max-width: 767px) {
		.error {
			font-size: 1em;
		}
	}
</style>
