import type { RequestHandler } from './$types';
import * as db from '$lib/server/database';
import { getEmail } from '$lib/utils/getEmail';

export const POST: RequestHandler = async ({ request, cookies }) => {
	const sessionCookie = cookies.get('user_session');
	const user_email = await getEmail(sessionCookie ?? '');
	const { survey_code, user_email_to_take_access_from } = await request.json();
	return db.takeAwayAccessToSurvey(user_email, survey_code, user_email_to_take_access_from);
};
