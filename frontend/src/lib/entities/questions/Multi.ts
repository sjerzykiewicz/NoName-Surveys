import Question from '$lib/entities/questions/Question';

export default class MultiQuestion extends Question {
	choices: Array<string>;
	answer: string | undefined;
	constructor(
		required: boolean = false,
		question: string = '',
		choices: Array<string> = [],
		answer: string | undefined
	) {
		super(required, question, 'multi');
		this.choices = choices;
		this.answer = answer;
	}
}
