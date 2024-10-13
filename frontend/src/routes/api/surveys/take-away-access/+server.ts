import type { RequestHandler } from './$types';
import * as db from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const { user_email, survey_code, user_email_to_take_access_from } = await request.json();
	return db.takeAwayAccessToSurvey(user_email, survey_code, user_email_to_take_access_from);
};
