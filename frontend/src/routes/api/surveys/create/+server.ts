import type { RequestHandler } from './$types';
import * as db from '$lib/server/database';
import type SurveyCreateInfo from '$lib/entities/surveys/SurveyCreateInfo';

export const POST: RequestHandler = async ({ request }) => {
	const info: SurveyCreateInfo = await request.json();
	return db.createSurvey(info);
};
