import type { RequestHandler } from './$types';
import { countSurveyDrafts } from '$lib/server/database';
import { getEmail } from '$lib/utils/getEmail';

export const GET: RequestHandler = async ({ cookies }) => {
	const sessionCookie = cookies.get('user_session');
	const user_email = await getEmail(sessionCookie ?? '');
	return countSurveyDrafts(user_email);
};
