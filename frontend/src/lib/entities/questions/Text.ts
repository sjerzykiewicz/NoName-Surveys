import Question from '$lib/entities/questions/Question';

class TextQuestionBody {
	details: string;
	constructor(details: string = '') {
		this.details = details;
	}
}

export default class TextQuestion extends Question {
	text: TextQuestionBody;
	constructor(required: boolean = false, question: string = '', details: string = '') {
		super(required, question);
		this.text = new TextQuestionBody(details);
	}
}
