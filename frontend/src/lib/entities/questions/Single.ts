import Question from '$lib/entities/questions/Question';

export class SingleQuestion extends Question {
	choices: Array<string>;
	constructor(required: boolean, question: string, choices: Array<string>) {
		super(required, question, 'single');
		this.choices = choices;
	}
}

export class SingleQuestionAnswered extends SingleQuestion {
	answer: string;
	constructor(required: boolean, question: string, choices: Array<string>, answer: string) {
		super(required, question, choices);
		this.answer = answer;
	}

	getAnswer(): string {
		return this.answer ? this.answer : '';
	}
}
