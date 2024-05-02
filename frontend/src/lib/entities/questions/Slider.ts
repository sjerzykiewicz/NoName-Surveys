import Question from '$lib/entities/questions/Question';

export default class SliderQuestion extends Question {
	min_value: number;
	max_value: number;
	answer: number | undefined;
	constructor(
		required: boolean = false,
		question: string = '',
		min_value: number = 0,
		max_value: number = 0,
		answer: number | undefined
	) {
		super(required, question, 'slider');
		this.min_value = min_value;
		this.max_value = max_value;
		this.answer = answer;
	}
}
