<script lang="ts">
	import { SurveyError } from '$lib/entities/SurveyError';
	import { questions } from '$lib/stores/create-page';
	import { LIMIT_OF_CHARS } from '$lib/stores/global';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import Subtitle from './Subtitle.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let questionIndex: number;

	$: displayIndex =
		questionIndex +
		1 -
		$questions.slice(0, questionIndex).filter((q) => q.component === Subtitle).length;

	function errorMessage(i: number) {
		const error = $questions[i].error;
		switch (error) {
			case SurveyError.ChoicesRequired:
				return $t('choice_error_required', { index: displayIndex });
			case SurveyError.BinaryChoicesRequired:
				return $t('choice_error_binary_required', { index: displayIndex });
			case SurveyError.NumberValuesRequired:
				return $t('choice_error_number_required', { index: displayIndex });
			case SurveyError.SliderValuesRequired:
				return $t('choice_error_slider_required', { index: displayIndex });
			case SurveyError.ChoicesTooLong:
				return $t('choice_error_limit', { index: displayIndex, limit: $LIMIT_OF_CHARS });
			case SurveyError.DuplicateChoices:
				return $t('choice_error_duplicate', { index: displayIndex });
			case SurveyError.ImproperSliderValues:
				return $t('choice_error_slider_values', { index: displayIndex });
			case SurveyError.ImproperSliderPrecision:
				return $t('choice_error_slider_precision', { index: displayIndex });
		}
	}

	$: checkChoiceError = (i: number) => {
		const error = $questions[i].error;
		switch (error) {
			case SurveyError.ChoicesRequired:
			case SurveyError.BinaryChoicesRequired:
			case SurveyError.NumberValuesRequired:
			case SurveyError.SliderValuesRequired:
				return $questions[i].choices.some(
					(c) => c === null || c === undefined || c.toString().trim().length === 0
				);
			case SurveyError.ChoicesTooLong:
				return $questions[i].choices.some((c) => c.length > $LIMIT_OF_CHARS);
			case SurveyError.DuplicateChoices:
				return new Set($questions[i].choices).size !== $questions[i].choices.length;
			case SurveyError.ImproperSliderValues:
				return parseFloat($questions[i].choices[0]) >= parseFloat($questions[i].choices[1]);
			case SurveyError.ImproperSliderPrecision:
				return (
					parseFloat($questions[i].choices[2]) >
					parseFloat($questions[i].choices[1]) - parseFloat($questions[i].choices[0])
				);
		}
	};
</script>

<div transition:slide={{ duration: 200, easing: cubicInOut }}>
	{#if checkChoiceError(questionIndex)}
		<p title={$t('error')} class="error" transition:slide={{ duration: 200, easing: cubicInOut }}>
			<i class="symbol">error</i>
			{#key [$t, $questions[questionIndex].error]}
				{errorMessage(questionIndex)}
			{/key}
		</p>
	{/if}
</div>

<style>
	.error {
		margin-top: 0.5em;
		margin-left: 2.8em;
	}
</style>
