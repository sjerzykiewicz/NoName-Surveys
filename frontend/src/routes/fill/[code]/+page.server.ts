import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ fetch, params }) => {
	const survey_code = params.code;
	const response = await fetch('http://localhost:8000/surveys', {
		method: 'POST',
		body: JSON.stringify({ survey_code }),
		headers: {
			'Content-Type': 'application/json'
		}
	});
	// TODO - error checks
	if (!response.ok) {
		return error(404);
	}
	const survey = (await response.json()).survey_structure;

	return {
		title: survey.title,
		questions: survey.questions
	};
};
