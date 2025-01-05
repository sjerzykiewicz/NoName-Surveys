import type { RequestHandler } from './$types';
import { getSurveyRespondents } from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const { survey_code, page }: { survey_code: string; page: number } = await request.json();
	return getSurveyRespondents(survey_code, page);
};
