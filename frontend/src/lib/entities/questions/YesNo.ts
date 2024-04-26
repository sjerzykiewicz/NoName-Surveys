import Question from '$lib/entities/questions/Question';

class YesNoQuestionBody {}

export default class YesNoQuestion extends Question {
	yes_no: YesNoQuestionBody = {};
	constructor(required: boolean = false, question: string = '') {
		super(required, question);
	}
}
