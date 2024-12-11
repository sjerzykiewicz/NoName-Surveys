import Question from '$lib/entities/questions/Question';
import Subtitle from '$lib/entities/questions/Subtitle';

export default class Survey {
	questions: Array<Question | Subtitle>;
	constructor(questions: Array<Question | Subtitle>) {
		this.questions = questions;
	}
}
