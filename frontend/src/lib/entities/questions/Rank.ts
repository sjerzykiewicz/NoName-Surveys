import Question from '$lib/entities/questions/Question';

export default class RankQuestion extends Question {
	choices: Array<string>;
	constructor(required: boolean = false, question: string = '', choices: Array<string> = []) {
		super(required, question, 'rank');
		this.choices = choices;
	}
}
