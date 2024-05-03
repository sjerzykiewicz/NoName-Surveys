import Question from '$lib/entities/questions/Question';

export default class RankQuestion extends Question {
	choices: Array<string>;
	answer: string | undefined;
	constructor(
		required: boolean = false,
		question: string = '',
		choices: Array<string> = [],
		answer: string | undefined
	) {
		super(required, question, 'rank');
		this.choices = choices;
		this.answer = answer;
	}
}
