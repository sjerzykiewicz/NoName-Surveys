import type { RequestHandler } from './$types';
import { deleteSurveyDraft } from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const { user_email, id } = await request.json();
	return deleteSurveyDraft(user_email, id);
};
