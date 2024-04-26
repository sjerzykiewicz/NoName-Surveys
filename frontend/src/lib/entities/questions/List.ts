import Question from '$lib/entities/questions/Question';

class ListQuestionBody {
	choices: Array<string>;
	constructor(choices: Array<string> = []) {
		this.choices = choices;
	}
}

export default class ListQuestion extends Question {
	list: ListQuestionBody;
	constructor(required: boolean = false, question: string = '', choices: Array<string> = []) {
		super(required, question);
		this.list = new ListQuestionBody(choices);
	}
}
