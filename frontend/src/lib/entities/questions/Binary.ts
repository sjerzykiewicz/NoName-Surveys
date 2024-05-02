import Question from '$lib/entities/questions/Question';

class BinaryQuestionBody {}

export default class BinaryQuestion extends Question {
	binary: BinaryQuestionBody = {};
	constructor(required: boolean = false, question: string = '') {
		super(required, question);
	}
}
