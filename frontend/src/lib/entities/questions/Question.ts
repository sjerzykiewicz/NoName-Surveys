export default class Question {
	required: boolean;
	question: string;
	constructor(required: boolean = false, question: string = '') {
		this.required = required;
		this.question = question;
	}
}
