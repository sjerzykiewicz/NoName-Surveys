import type Question from '$lib/entities/questions/Question';

export class SurveyAnswer {
	survey_code: string;
	questions: Array<Question>;
	signature: string[];
	constructor(survey_code: string, questions: Array<Question>, signature: string[] = []) {
		this.survey_code = survey_code;
		this.questions = questions;
		this.signature = signature;
	}
}
