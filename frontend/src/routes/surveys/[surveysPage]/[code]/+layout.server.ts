import type { LayoutServerLoad } from './$types';
import { error } from '@sveltejs/kit';
import Survey from '$lib/entities/surveys/Survey';
import SurveySummary from '$lib/entities/surveys/SurveySummary';

export const load: LayoutServerLoad = async ({ parent, params, url }) => {
	const { session } = await parent();
	if (!session) {
		error(401, 'You must be logged in to access this page.');
	}

	const code = params.code;
	const host = url.origin;

	const surveyResponse = await fetch(`${host}/api/surveys/fetch`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ survey_code: code })
	});
	if (!surveyResponse.ok) {
		error(surveyResponse.status, { message: await surveyResponse.json() });
	}
	const survey: {
		title: string;
		survey_structure: Survey;
		survey_code: string;
		uses_cryptographic_module: boolean;
		public_keys: string[];
	} = await surveyResponse.json();

	const answersResponse = await fetch(`${host}/api/surveys/answers/fetch`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ survey_code: code })
	});
	if (!answersResponse.ok) {
		error(answersResponse.status, { message: await answersResponse.json() });
	}
	const answers: Array<SurveySummary> = await answersResponse.json();

	const { surveys } = await parent();
	const survey_index = surveys.findIndex((s) => s.survey_code === survey.survey_code);

	return { survey, answers, survey_index };
};
