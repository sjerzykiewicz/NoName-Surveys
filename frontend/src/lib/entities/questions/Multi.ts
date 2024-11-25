import Question from '$lib/entities/questions/Question';

export class MultiQuestion extends Question {
	choices: Array<string>;
	constructor(required: boolean, question: string, choices: Array<string>) {
		super(required, question, 'multi');
		this.choices = choices;
	}
}

export class MultiQuestionAnswered extends MultiQuestion {
	answer: Array<string>;
	constructor(required: boolean, question: string, choices: Array<string>, answer: Array<string>) {
		super(required, question, choices);
		this.answer = answer;
	}

	getAnswer(): string {
		return this.answer ? this.answer.join('') : '';
	}
}
