import Question from '$lib/entities/questions/Question';

export class TextQuestion extends Question {
	details: string;
	constructor(required: boolean, question: string, details: string) {
		super(required, question, 'text');
		this.details = details;
	}
}

export class TextQuestionAnswered extends TextQuestion {
	answer: string;
	constructor(required: boolean, question: string, details: string, answer: string) {
		super(required, question, details);
		this.answer = answer;
	}

	getAnswer(): string {
		return this.answer;
	}
}
