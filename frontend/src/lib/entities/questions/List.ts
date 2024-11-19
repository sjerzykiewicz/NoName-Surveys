import Question from '$lib/entities/questions/Question';

export class ListQuestion extends Question {
	choices: Array<string>;
	constructor(required: boolean, question: string, choices: Array<string>) {
		super(required, question, 'list');
		this.choices = choices;
	}
}

export class ListQuestionAnswered extends ListQuestion {
	answer: string;
	constructor(required: boolean, question: string, choices: Array<string>, answer: string) {
		super(required, question, choices);
		this.answer = answer;
	}

	getAnswer(): string {
		return this.answer.toString();
	}
}
