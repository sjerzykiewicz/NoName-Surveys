import type { RequestHandler } from './$types';
import * as db from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const { survey_code } = await request.json();
	return db.getSurveyRespondentsByCode(survey_code);
};
