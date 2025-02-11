export default class Question {
	required: boolean;
	question: string;
	question_type: string;
	constructor(required: boolean, question: string, question_type: string) {
		this.required = required;
		this.question = question;
		this.question_type = question_type;
	}

	// Default implementation that is to be overridden by subclasses
	getAnswer(): string {
		return '';
	}
}
