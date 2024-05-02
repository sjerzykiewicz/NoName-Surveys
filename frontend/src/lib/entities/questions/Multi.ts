import Question from '$lib/entities/questions/Question';

export default class MultiQuestion extends Question {
	choices: Array<string>;
	constructor(required: boolean = false, question: string = '', choices: Array<string> = []) {
		super(required, question, 'multi');
		this.choices = choices;
	}
}
