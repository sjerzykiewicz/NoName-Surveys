import Question from '$lib/entities/questions/Question';

export default class TextQuestion extends Question {
	details: string;
	answer: string | undefined;
	constructor(
		required: boolean = false,
		question: string = '',
		details: string = '',
		answer: string | undefined
	) {
		super(required, question, 'text');
		this.details = details;
		this.answer = answer;
	}
}
