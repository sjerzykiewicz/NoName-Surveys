import Question from '$lib/entities/questions/Question';

export class NumberQuestion extends Question {
	min_value: number;
	max_value: number;
	constructor(required: boolean, question: string, min_value: number, max_value: number) {
		super(required, question, 'number');
		this.min_value = min_value;
		this.max_value = max_value;
	}
}

export class NumberQuestionAnswered extends NumberQuestion {
	answer: number;
	constructor(
		required: boolean,
		question: string,
		min_value: number,
		max_value: number,
		answer: number
	) {
		super(required, question, min_value, max_value);
		this.answer = answer;
	}

	getAnswer(): string {
		return this.answer.toString();
	}
}
