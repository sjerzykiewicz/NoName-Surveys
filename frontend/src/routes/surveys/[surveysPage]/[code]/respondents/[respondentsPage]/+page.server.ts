import type { PageServerLoad } from './$types';
import { error } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ params, fetch }) => {
	const code = params.code;
	const page = parseInt(params.respondentsPage);

	const respondentsResponse = await fetch(`/api/surveys/respondents/all`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ survey_code: code, page })
	});
	if (!respondentsResponse.ok) {
		error(respondentsResponse.status, { message: await respondentsResponse.json() });
	}
	const respondents: string[] = await respondentsResponse.json();

	const countResponse = await fetch(`/api/surveys/respondents/count`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ survey_code: code })
	});
	if (!countResponse.ok) {
		error(countResponse.status, { message: await countResponse.json() });
	}
	const numRespondents: number = await countResponse.json();

	return { respondents, numRespondents };
};
