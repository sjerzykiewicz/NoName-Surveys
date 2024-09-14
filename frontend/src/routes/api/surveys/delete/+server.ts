import type { RequestHandler } from './$types';
import * as db from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const { user_email, survey_code } = await request.json();
	return db.deleteSurveyByCode(user_email, survey_code);
};
