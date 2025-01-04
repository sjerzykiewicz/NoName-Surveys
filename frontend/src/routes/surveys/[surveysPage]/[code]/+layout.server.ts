import type { LayoutServerLoad } from './$types';
import { error } from '@sveltejs/kit';
import type Survey from '$lib/entities/surveys/Survey';
import type SurveySummary from '$lib/entities/surveys/SurveySummary';

export const load: LayoutServerLoad = async ({ parent, params, fetch }) => {
	const { session, surveys } = await parent();
	if (!session) {
		error(401, 'You must be logged in to access this page.');
	}

	const code = params.code;

	try {
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

		const survey_index = surveys.findIndex((s) => s.survey_code === survey.survey_code);

		return { survey, answers, survey_index };
	} catch (err) {
		console.error(err);
		throw error(500, { message: 'Failed to fetch data after multiple attempts' });
	}
};
