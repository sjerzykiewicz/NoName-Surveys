import Question from '$lib/entities/questions/Question';

export default class SliderQuestion extends Question {
	min_value: number;
	max_value: number;
	constructor(
		required: boolean = false,
		question: string = '',
		min_value: number = 0,
		max_value: number = 0
	) {
		super(required, question, 'slider');
		this.min_value = min_value;
		this.max_value = max_value;
	}
}
