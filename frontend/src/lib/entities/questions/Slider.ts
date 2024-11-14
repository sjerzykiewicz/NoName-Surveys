import Question from '$lib/entities/questions/Question';

export class SliderQuestion extends Question {
	min_value: number;
	max_value: number;
	precision: number;
	constructor(
		required: boolean,
		question: string,
		min_value: number,
		max_value: number,
		precision: number
	) {
		super(required, question, 'slider');
		this.min_value = min_value;
		this.max_value = max_value;
		this.precision = precision;
	}
}

export class SliderQuestionAnswered extends SliderQuestion {
	answer: number;
	constructor(
		required: boolean,
		question: string,
		min_value: number,
		max_value: number,
		precision: number,
		answer: number
	) {
		super(required, question, min_value, max_value, precision);
		this.answer = answer;
	}
}
