import Question from '$lib/entities/questions/Question';

export default class YesNoQuestion extends Question {
	choices: Array<string>;
	answer: string | undefined;
	constructor(
		required: boolean = false,
		question: string = '',
		choices: Array<string> = [],
		answer: string | undefined
	) {
		super(required, question, 'binary');
		this.choices = choices;
		this.answer = answer;
	}
}
