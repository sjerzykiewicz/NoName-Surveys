import type Question from '$lib/entities/questions/Question';
import type Subtitle from '$lib/entities/questions/Subtitle';

export default class SurveySummary {
	title: string;
	questions: Array<Question | Subtitle>;
	constructor(title: string, questions: Array<Question | Subtitle>) {
		this.title = title;
		this.questions = questions;
	}
}
