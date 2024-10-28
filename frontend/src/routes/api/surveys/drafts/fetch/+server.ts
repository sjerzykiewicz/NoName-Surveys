import type { RequestHandler } from './$types';
import { getSurveyDraft } from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const { user_email, id } = await request.json();
	return getSurveyDraft(user_email, id);
};
