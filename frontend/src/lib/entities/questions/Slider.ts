import Question from '$lib/entities/questions/Question';

class SliderQuestionBody {
	min_value: number;
	max_value: number;
	constructor(min_value: number = 0, max_value: number = 0) {
		this.min_value = min_value;
		this.max_value = max_value;
	}
}

export default class SliderQuestion extends Question {
	slider: SliderQuestionBody;
	constructor(
		required: boolean = false,
		question: string = '',
		min_value: number = 0,
		max_value: number = 0
	) {
		super(required, question);
		this.slider = new SliderQuestionBody(min_value, max_value);
	}
}
