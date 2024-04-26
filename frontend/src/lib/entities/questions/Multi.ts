import Question from '$lib/entities/questions/Question';

class MultiQuestionBody {
	choices: Array<string>;
	constructor(choices: Array<string> = []) {
		this.choices = choices;
	}
}

export default class MultiQuestion extends Question {
	multi: MultiQuestionBody;
	constructor(required: boolean = false, question: string = '', choices: Array<string> = []) {
		super(required, question);
		this.multi = new MultiQuestionBody(choices);
	}
}
