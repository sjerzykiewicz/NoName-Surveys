import QuestionsStore from '$lib/entities/questions/QuestionsStore';

export function trimQuestions(questions: Array<QuestionsStore>): Array<QuestionsStore> {
	return questions.map((q) => {
		q.component;
		q.preview;
		q.required;
		q.question = q.question.trim().replace(/\n\s*\n/g, '\n\n');
		q.choices = q.choices.map((c) => {
			if (typeof c === 'string') return c.trim().replace(/\n\s*\n/g, '\n\n');
			return c;
		});
		q.error;
		return q;
	});
}
