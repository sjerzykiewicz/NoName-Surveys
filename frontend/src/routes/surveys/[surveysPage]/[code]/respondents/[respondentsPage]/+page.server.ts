import type { PageServerLoad } from './$types';
import { getSurveyRespondents, countSurveyRespondents } from '$lib/server/database';
import { error } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ params }) => {
	const code = params.code;
	const page = parseInt(params.respondentsPage);

	const respondentsResponse = await getSurveyRespondents(code, page);
	if (!respondentsResponse.ok) {
		error(respondentsResponse.status, { message: await respondentsResponse.json() });
	}
	const respondents: string[] = await respondentsResponse.json();

	const countResponse = await countSurveyRespondents(code);
	if (!countResponse.ok) {
		error(countResponse.status, { message: await countResponse.json() });
	}
	const numRespondents: number = await countResponse.json();

	return { respondents, numRespondents };
};
