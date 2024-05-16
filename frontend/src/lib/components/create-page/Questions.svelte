<script lang="ts">
	import QuestionButtons from '$lib/components/create-page/QuestionButtons.svelte';
	import QuestionTitle from '$lib/components/create-page/QuestionTitle.svelte';
	import { QuestionError } from '$lib/entities/QuestionError';
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { scrollToElement } from '$lib/utils/scrollToElement';

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

	$: checkQuestionError = (i: number) => {
		return $questions[i].error === QuestionError.QuestionRequired && !$questions[i].question;
	};

	$: checkChoicesError = (i: number) => {
		const error = $questions[i].error;
		switch (error) {
			case QuestionError.ChoicesRequired:
			case QuestionError.BinaryChoicesRequired:
			case QuestionError.SliderValuesRequired:
				if ($questions[i].choices.some((c) => !c)) {
					return true;
				}
				break;
			case QuestionError.DuplicateChoices:
				if (new Set($questions[i].choices).size !== $questions[i].choices.length) {
					return true;
				}
				break;
			case QuestionError.ImproperSliderValues:
				if (parseFloat($questions[i].choices[0]) >= parseFloat($questions[i].choices[1])) {
					return true;
				}
				break;
		}
		return false;
	};
</script>

{#each $questions as question, questionIndex}
	<div
		class="question"
		in:slide={{ duration: 200, easing: cubicInOut }}
		on:introend={() => scrollToElement('.add-question')}
	>
		<QuestionTitle {questionIndex} questionType={question.component} />

		{#key question.error}
			{#if checkQuestionError(questionIndex)}
				<p title="Error" class="error question-error">
					<i class="material-symbols-rounded">error</i>{errorMessage(questionIndex)}
				</p>
			{/if}

			<svelte:component this={question.component} {questionIndex} />

			{#if checkChoicesError(questionIndex)}
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
