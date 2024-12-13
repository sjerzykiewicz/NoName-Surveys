import type { LayoutServerLoad } from './$types';
import { error, redirect } from '@sveltejs/kit';
import type SurveyHeader from '$lib/entities/surveys/SurveyHeader';

export const load: LayoutServerLoad = async ({ parent, params, fetch }) => {
	const { session } = await parent();
	if (!session) {
		redirect(303, `/account`);
	}

	const page = parseInt(params.surveysPage);

	const surveysResponse = await fetch(`/api/surveys/all`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ page })
	});
	if (!surveysResponse.ok) {
		error(surveysResponse.status, { message: await surveysResponse.json() });
	}
	const surveys: SurveyHeader[] = await surveysResponse.json();

	const countResponse = await fetch(`/api/surveys/count`);
	if (!countResponse.ok) {
		error(countResponse.status, { message: await countResponse.json() });
	}
	const numSurveys: number = await countResponse.json();

	return { surveys, numSurveys };
};
