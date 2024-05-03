import type { PageLoad } from '../$types';

export const load: PageLoad = async () => {
	const response = await fetch('http://localhost:8000/survey-drafts/all', { method: 'GET' });
	const surveys = await response.json();
	// TODO - for now return the first survey
	return surveys[0].survey_structure;
};
