import type { RequestHandler } from './$types';
import { createSurvey } from '$lib/server/database';
import type SurveyCreateInfo from '$lib/entities/surveys/SurveyCreateInfo';

export const POST: RequestHandler = async ({ request }) => {
	const info: SurveyCreateInfo = await request.json();
	return createSurvey(info);
};
