import type { LayoutServerLoad } from './$types';
import { error, redirect } from '@sveltejs/kit';
import type SurveyHeader from '$lib/entities/surveys/SurveyHeader';

export const load: LayoutServerLoad = async ({ parent, params, fetch }) => {
	const { session } = await parent();
	if (!session) {
		redirect(303, `/account`);
	}

	const page = parseInt(params.surveysPage);

	try {
		const [surveysResponse, countResponse] = await Promise.all([
			fetch(`/api/surveys/all`, {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({ page })
			}),
			fetch(`/api/surveys/count`)
		]);

		if (!surveysResponse.ok) {
			throw error(surveysResponse.status, { message: await surveysResponse.json() });
		}
		const surveys: SurveyHeader[] = await surveysResponse.json();

		if (!countResponse.ok) {
			throw error(countResponse.status, { message: await countResponse.json() });
		}
		const numSurveys: number = await countResponse.json();

		return { surveys, numSurveys };
	} catch (err) {
		console.error(err);
		throw error(500, { message: 'Failed to fetch data' });
	}
};
