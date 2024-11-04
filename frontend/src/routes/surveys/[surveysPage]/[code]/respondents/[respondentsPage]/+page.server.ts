import type { PageServerLoad } from './$types';
import { getSurveyRespondents } from '$lib/server/database';
import { error } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ params }) => {
	const code = params.code;
	const page = parseInt(params.respondentsPage);

	const response = await getSurveyRespondents(code, page);
	if (!response.ok) {
		error(response.status, { message: await response.json() });
	}
	const respondents: string[] = await response.json();

	return { respondents };
};
