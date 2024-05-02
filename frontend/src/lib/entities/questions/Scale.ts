import Question from '$lib/entities/questions/Question';

export default class ScaleQuestion extends Question {
	answer: number | undefined;
	constructor(required: boolean = false, question: string = '', answer: number | undefined) {
		super(required, question, 'scale');
		this.answer = answer;
	}
}
