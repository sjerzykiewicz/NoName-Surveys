import QuestionsStore from '../entities/questions/QuestionsStore';
import { SurveyError } from '../entities/SurveyError';
import Binary from '../components/create-page/Binary.svelte';
import Number from '../components/create-page/Number.svelte';
import Slider from '../components/create-page/Slider.svelte';
import Text from '../components/create-page/Text.svelte';
import Subtitle from '../components/create-page/Subtitle.svelte';

export function checkQuestionError(question: QuestionsStore, limit: number) {
	if (question.component === Subtitle) {
		if (question.question.length > limit) {
			question.error = SurveyError.SubtitleTooLong;
		} else {
			question.error = SurveyError.NoError;
		}
		return;
	}

	const q = question.question;
	if (q === null || q === undefined || q.length === 0) {
		question.error = SurveyError.QuestionRequired;
	} else if (q.length > limit) {
		question.error = SurveyError.QuestionTooLong;
	} else if (
		question.component != Text &&
		question.choices.some((c) => c === null || c === undefined || c.toString().length === 0)
	) {
		switch (question.component) {
			case Number:
				question.error = SurveyError.NumberValuesRequired;
				break;
			case Slider:
				question.error = SurveyError.SliderValuesRequired;
				break;
			case Binary:
				question.error = SurveyError.BinaryChoicesRequired;
				break;
			default:
				question.error = SurveyError.ChoicesRequired;
		}
	} else if (question.choices.some((c) => c.length > limit)) {
		question.error = SurveyError.ChoicesTooLong;
	} else if (
		(question.component === Slider || question.component === Number) &&
		parseFloat(question.choices[0]) >= parseFloat(question.choices[1])
	) {
		question.error = SurveyError.ImproperSliderValues;
	} else if (
		question.component === Slider &&
		parseFloat(question.choices[2]) >
			parseFloat(question.choices[1]) - parseFloat(question.choices[0])
	) {
		question.error = SurveyError.ImproperSliderPrecision;
	} else if (
		question.component !== Slider &&
		new Set(question.choices).size !== question.choices.length
	) {
		question.error = SurveyError.DuplicateChoices;
	} else {
		question.error = SurveyError.NoError;
	}
}
