import type { LayoutServerLoad } from './$types';
import { error } from '@sveltejs/kit';
import Survey from '$lib/entities/surveys/Survey';
import SurveySummary from '$lib/entities/surveys/SurveySummary';

export const load: LayoutServerLoad = async ({ parent, params, fetch }) => {
	const { session, surveys } = await parent();
	if (!session) {
		error(401, 'You must be logged in to access this page.');
	}

	const code = params.code;

	const [surveyResponse, answersResponse] = await Promise.all([
		fetch(`/api/surveys/fetch`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ survey_code: code })
		}),
		fetch(`/api/surveys/answers/fetch`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ survey_code: code })
		})
	]);

	if (!surveyResponse.ok) {
		throw error(surveyResponse.status, { message: await surveyResponse.json() });
	}
	const survey: {
		title: string;
		survey_structure: Survey;
		survey_code: string;
		uses_cryptographic_module: boolean;
		public_keys: string[];
	} = await surveyResponse.json();

	if (!answersResponse.ok) {
		throw error(answersResponse.status, { message: await answersResponse.json() });
	}
	const answers: Array<SurveySummary> = await answersResponse.json();

	const survey_index: number = surveys.findIndex((s) => s.survey_code === survey.survey_code);

	return { survey, answers, survey_index };
};
