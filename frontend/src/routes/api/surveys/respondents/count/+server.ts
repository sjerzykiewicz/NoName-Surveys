import type { RequestHandler } from './$types';
import { countSurveyRespondents } from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const { survey_code }: { survey_code: string } = await request.json();
	return countSurveyRespondents(survey_code);
};
