import Question from '$lib/entities/questions/Question';

export class RankQuestion extends Question {
	choices: Array<string>;
	constructor(required: boolean, question: string, choices: Array<string>) {
		super(required, question, 'rank');
		this.choices = choices;
	}
}

export class RankQuestionAnswered extends RankQuestion {
	answer: Array<string>;
	constructor(required: boolean, question: string, choices: Array<string>, answer: Array<string>) {
		super(required, question, choices);
		this.answer = answer;
	}

	getAnswer(): string {
		return this.answer.toString();
	}
}
