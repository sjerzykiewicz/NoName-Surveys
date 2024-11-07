<script lang="ts">
	import { SurveyError } from '$lib/entities/SurveyError';
	import { questions } from '$lib/stores/create-page';
	import { LIMIT_OF_CHARS } from '$lib/stores/global';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	export let questionIndex: number;

	function errorMessage(i: number) {
		const error = $questions[i].error;
		switch (error) {
			case SurveyError.ChoicesRequired:
				return 'Please enter all choices for question no. ' + (i + 1) + '.';
			case SurveyError.BinaryChoicesRequired:
				return 'Please enter both choices for question no. ' + (i + 1) + '.';
			case SurveyError.SliderValuesRequired:
				return 'Please enter both values for question no. ' + (i + 1) + '.';
			case SurveyError.ChoicesTooLong:
				return (
					'Choices must be ' +
					$LIMIT_OF_CHARS +
					' or less characters long in question no. ' +
					(i + 1) +
					'.'
				);
			case SurveyError.DuplicateChoices:
				return 'Please remove duplicate choices from question no. ' + (i + 1) + '.';
			case SurveyError.ImproperSliderValues:
				return 'Maximum value must be greater than minimum value in question no. ' + (i + 1) + '.';
		}
	}

	$: checkChoicesError = (i: number) => {
		const error = $questions[i].error;
		switch (error) {
			case SurveyError.ChoicesRequired:
			case SurveyError.BinaryChoicesRequired:
			case SurveyError.SliderValuesRequired:
				return $questions[i].choices.some(
					(c) => c === null || c === undefined || c.trim().length === 0
				);
			case SurveyError.ChoicesTooLong:
				return $questions[i].choices.some((c) => c.length > $LIMIT_OF_CHARS);
			case SurveyError.DuplicateChoices:
				return new Set($questions[i].choices).size !== $questions[i].choices.length;
			case SurveyError.ImproperSliderValues:
				return parseFloat($questions[i].choices[0]) >= parseFloat($questions[i].choices[1]);
		}
	};
</script>

<div
	in:slide={{ delay: 200, duration: 200, easing: cubicInOut }}
	out:slide={{ duration: 200, easing: cubicInOut }}
>
	{#if checkChoicesError(questionIndex)}
		<p title="Error" class="error" transition:slide={{ duration: 200, easing: cubicInOut }}>
			<i class="symbol">error</i>{errorMessage(questionIndex)}
		</p>
	{/if}
</div>

<style>
	.error {
		margin-top: 0.5em;
		margin-left: 2.8em;
	}
</style>
