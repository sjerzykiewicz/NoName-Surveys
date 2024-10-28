import type { RequestHandler } from './$types';
import { giveAccessToSurvey } from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const { user_email, survey_code, user_emails_to_share_with } = await request.json();
	return giveAccessToSurvey(user_email, survey_code, user_emails_to_share_with);
};
