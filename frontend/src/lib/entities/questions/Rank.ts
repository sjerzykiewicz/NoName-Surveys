import Question from '$lib/entities/questions/Question';

class RankQuestionBody {
	choices: Array<string>;
	constructor(choices: Array<string> = []) {
		this.choices = choices;
	}
}

export default class RankQuestion extends Question {
	rank: RankQuestionBody;
	constructor(required: boolean = false, question: string = '', choices: Array<string> = []) {
		super(required, question);
		this.rank = new RankQuestionBody(choices);
	}
}
