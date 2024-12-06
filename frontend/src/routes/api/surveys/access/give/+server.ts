import type { RequestHandler } from './$types';
import { giveAccessToSurvey } from '$lib/server/database';
import { getEmail } from '$lib/utils/getEmail';

export const POST: RequestHandler = async ({ request, cookies }) => {
	const sessionCookie = cookies.get('user_session');
	const user_email = await getEmail(sessionCookie ?? '');
	const { survey_code, user_emails }: { survey_code: string; user_emails: string[] } =
		await request.json();
	return giveAccessToSurvey(user_email, survey_code, user_emails);
};
