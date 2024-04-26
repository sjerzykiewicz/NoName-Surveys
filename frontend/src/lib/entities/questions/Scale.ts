import Question from '$lib/entities/questions/Question';

class ScaleQuestionBody {}

export default class ScaleQuestion extends Question {
	scale: ScaleQuestionBody = {};
	constructor(required: boolean = false, question: string = '') {
		super(required, question);
	}
}
