import Question from '$lib/entities/questions/Question';

export default class Survey {
	questions: Array<Question>;
	constructor(questions: Array<Question>) {
		this.questions = questions;
	}
}
