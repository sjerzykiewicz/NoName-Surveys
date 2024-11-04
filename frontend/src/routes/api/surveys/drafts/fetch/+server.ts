import type { RequestHandler } from './$types';
import { getSurveyDraft } from '$lib/server/database';
import { getEmail } from '$lib/utils/getEmail';

export const POST: RequestHandler = async ({ request, cookies }) => {
	const sessionCookie = cookies.get('user_session');
	const user_email = await getEmail(sessionCookie ?? '');
	const { id } = await request.json();
	return getSurveyDraft(user_email, id);
};
