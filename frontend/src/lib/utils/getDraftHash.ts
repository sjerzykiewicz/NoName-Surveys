import QuestionsStore from '$lib/entities/questions/QuestionsStore';
import { getQuestionTypeData } from './getQuestionTypeData';
import pkg from 'crypto-js';
const { MD5 } = pkg;

export function getDraftHash(title: string, questions: Array<QuestionsStore>) {
	const data = {
		title: title,
		questions: questions.map((q) => ({
			component: getQuestionTypeData(q.component).text,
			question: q.question,
			choices: q.choices,
			required: q.required,
			error: q.error
		}))
	};
	return MD5(JSON.stringify(data)).toString();
}
