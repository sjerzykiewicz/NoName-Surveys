import Question from '$lib/entities/questions/Question';

export default class Survey {
	title: string;
	questions: Array<Question>;
	constructor(title: string = '', questions: Array<Question> = []) {
		this.title = title;
		this.questions = questions;
	}
}
