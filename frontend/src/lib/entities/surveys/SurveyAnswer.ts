import type Question from '$lib/entities/questions/Question';

export class SurveyAnswer {
	survey_code: string;
	questions: Array<Question>;
	constructor(survey_code: string, questions: Array<Question>) {
		this.survey_code = survey_code;
		this.questions = questions;
	}
}
