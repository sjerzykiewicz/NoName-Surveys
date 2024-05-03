import type { PageLoad } from '../$types';

export const load: PageLoad = async () => {
	const response = await fetch('http://localhost:8000/survey-drafts/all', { method: 'GET' });
	const surveys = await response.json();
	// TODO - for now return the first survey
	if (surveys.length === 0) {
		return {
			title: '',
			questions: []
		};
	} else {
		const first = surveys[0].survey_structure;
		return {
			title: first.title,
			questions: first.questions
		};
	}
};
