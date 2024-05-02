import Question from '$lib/entities/questions/Question';

export default class ScaleQuestion extends Question {
	constructor(required: boolean = false, question: string = '') {
		super(required, question, 'scale');
	}
}
