import type { RequestHandler } from './$types';
import { takeAwayAccessToSurvey } from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const { user_email, survey_code, user_email_to_take_access_from } = await request.json();
	return takeAwayAccessToSurvey(user_email, survey_code, user_email_to_take_access_from);
};
