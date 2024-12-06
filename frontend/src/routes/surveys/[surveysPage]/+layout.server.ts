import type { LayoutServerLoad } from './$types';
import { error, redirect } from '@sveltejs/kit';

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
	const surveys: {
		title: string;
		survey_code: string;
		creation_date: string;
		uses_cryptographic_module: boolean;
		is_owned_by_user: boolean;
		group_size: number;
	}[] = await surveysResponse.json();

	const countResponse = await fetch(`/api/surveys/count`);
	if (!countResponse.ok) {
		error(countResponse.status, { message: await countResponse.json() });
	}
	const numSurveys: number = await countResponse.json();

	return { surveys, numSurveys };
};
