import QuestionsStore from '$lib/entities/questions/QuestionsStore';
import { getQuestionTypeData } from './getQuestionTypeData';

export function getDraft(title: string, questions: Array<QuestionsStore>) {
	return JSON.stringify({
		title: title,
		questions: questions.map((q) => ({
			component: getQuestionTypeData(q.component).text,
			question: q.question,
			choices: q.choices,
			required: q.required,
			error: q.error
		}))
	});
}
