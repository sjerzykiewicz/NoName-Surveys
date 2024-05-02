import Question from '$lib/entities/questions/Question';

export default class ListQuestion extends Question {
	choices: Array<string>;
	constructor(required: boolean = false, question: string = '', choices: Array<string> = []) {
		super(required, question, 'list');
		this.choices = choices;
	}
}
