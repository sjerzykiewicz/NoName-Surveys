import Question from '$lib/entities/questions/Question';

export class BinaryQuestion extends Question {
	choices: Array<string>;
	constructor(required: boolean, question: string, choices: Array<string>) {
		super(required, question, 'binary');
		this.choices = choices;
	}
}

export class BinaryQuestionAnswered extends BinaryQuestion {
	answer: string;
	constructor(required: boolean, question: string, choices: Array<string>, answer: string) {
		super(required, question, choices);
		this.answer = answer;
	}

	getAnswer(): string {
		return this.answer.toString();
	}
}
