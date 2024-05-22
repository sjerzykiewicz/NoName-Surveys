<script lang="ts">
	import { QuestionError } from '$lib/entities/QuestionError';
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	export let questionIndex: number;

	function errorMessage(i: number) {
		const error = $questions[i].error;
		switch (error) {
			case QuestionError.BinaryChoicesRequired:
				return 'Please enter both choices for question no. ' + (i + 1) + '.';
			case QuestionError.SliderValuesRequired:
				return 'Please enter both values for question no. ' + (i + 1) + '.';
			case QuestionError.DuplicateChoices:
				return 'Please remove duplicate choices from question no. ' + (i + 1) + '.';
			case QuestionError.ImproperSliderValues:
				return 'Maximum value must be greater than minimum value in question no. ' + (i + 1) + '.';
			default:
				return 'Please enter all choices for question no. ' + (i + 1) + '.';
		}
	}

	$: checkChoicesError = (i: number) => {
		const error = $questions[i].error;
		switch (error) {
			case QuestionError.ChoicesRequired:
			case QuestionError.BinaryChoicesRequired:
			case QuestionError.SliderValuesRequired:
				if ($questions[i].choices.some((c) => c === null || c === undefined || c.length === 0)) {
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

{#if checkChoicesError(questionIndex)}
	<p
		title="Error"
		class="error choice-error"
		transition:slide={{ duration: 200, easing: cubicInOut }}
	>
		<i class="material-symbols-rounded">error</i>{errorMessage(questionIndex)}
	</p>
{/if}

<style>
	.error {
		margin-left: 2.8em;
	}

	.choice-error {
		margin-top: 0.5em;
	}
</style>
