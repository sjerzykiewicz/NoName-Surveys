import type Question from '$lib/entities/questions/Question';

export default class SurveySummary {
	title: string;
	questions: Array<Question>;
	is_owned_by_user: boolean;
	constructor(title: string, questions: Array<Question>, is_owned_by_user: boolean) {
		this.title = title;
		this.questions = questions;
		this.is_owned_by_user = is_owned_by_user;
	}
}
