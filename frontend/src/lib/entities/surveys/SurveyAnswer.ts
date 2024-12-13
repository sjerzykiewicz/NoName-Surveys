import type Question from '$lib/entities/questions/Question';
import type Subtitle from '$lib/entities/questions/Subtitle';

export default class SurveyAnswer {
	survey_code: string;
	questions: Array<Question | Subtitle>;
	signature: string[];
	constructor(
		survey_code: string,
		questions: Array<Question | Subtitle>,
		signature: string[] = []
	) {
		this.survey_code = survey_code;
		this.questions = questions;
		this.signature = signature;
	}
}
