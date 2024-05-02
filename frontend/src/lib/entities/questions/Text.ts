import Question from '$lib/entities/questions/Question';

export default class TextQuestion extends Question {
	details: string;
	constructor(required: boolean = false, question: string = '', details: string = '') {
		super(required, question, 'text');
		this.details = details;
	}
}
