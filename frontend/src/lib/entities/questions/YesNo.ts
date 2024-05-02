import Question from '$lib/entities/questions/Question';

export default class YesNoQuestion extends Question {
	choices: Array<string>;
	constructor(required: boolean = false, question: string = '', choices: Array<string> = []) {
		super(required, question, 'binary');
		this.choices = choices;
	}
}
