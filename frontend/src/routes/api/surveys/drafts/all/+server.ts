import type { RequestHandler } from './$types';
import { getSurveyDrafts } from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const { user_email } = await request.json();
	return getSurveyDrafts(user_email);
};
