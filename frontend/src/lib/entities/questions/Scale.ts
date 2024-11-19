import Question from '$lib/entities/questions/Question';

export class ScaleQuestion extends Question {
	constructor(required: boolean, question: string) {
		super(required, question, 'scale');
	}
}

export class ScaleQuestionAnswered extends ScaleQuestion {
	answer: number;
	constructor(required: boolean, question: string, answer: number) {
		super(required, question);
		this.answer = answer;
	}

	getAnswer(): string {
		return this.answer.toString();
	}
}
