import Question from '$lib/entities/questions/Question';

class SingleQuestionBody {
	choices: Array<string>;
	constructor(choices: Array<string> = []) {
		this.choices = choices;
	}
}

export default class SingleQuestion extends Question {
	single: SingleQuestionBody;
	constructor(required: boolean = false, question: string = '', choices: Array<string> = []) {
		super(required, question);
		this.single = new SingleQuestionBody(choices);
	}
}
