import Question from '$lib/entities/questions/Question';

export default class SingleQuestion extends Question {
	choices: Array<string>;
	constructor(required: boolean = false, question: string = '', choices: Array<string> = []) {
		super(required, question, 'single');
		this.choices = choices;
	}
}
