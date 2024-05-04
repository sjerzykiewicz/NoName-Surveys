import type { PageLoad } from '../$types';

export const load: PageLoad = async ({ fetch }) => {
	const response = await fetch('http://localhost:8000/survey-drafts/all/1', { method: 'GET' });
	const surveys = await response.json();
	// TODO - for now return the newest survey
	if (surveys.length === 0) {
		return {
			title: '',
			questions: []
		};
	} else {
		const first = surveys[surveys.length - 1].survey_structure;
		return {
			title: first.title,
			questions: first.questions
		};
	}
};
