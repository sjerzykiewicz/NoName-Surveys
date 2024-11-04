import type Question from '$lib/entities/questions/Question';

export default class SurveySummary {
	title: string;
	questions: Array<Question>;
	constructor(title: string, questions: Array<Question>) {
		this.title = title;
		this.questions = questions;
	}
}
