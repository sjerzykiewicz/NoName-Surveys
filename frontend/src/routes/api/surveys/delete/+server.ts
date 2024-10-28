import type { RequestHandler } from './$types';
import { deleteSurvey } from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const { user_email, survey_code } = await request.json();
	return deleteSurvey(user_email, survey_code);
};
