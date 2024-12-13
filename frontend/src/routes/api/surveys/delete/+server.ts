import type { RequestHandler } from './$types';
import { deleteSurveys } from '$lib/server/database';
import { getEmail } from '$lib/utils/getEmail';

export const POST: RequestHandler = async ({ request, cookies }) => {
	const sessionCookie = cookies.get('user_session');
	const user_email = await getEmail(sessionCookie ?? '');
	const { survey_codes }: { survey_codes: string[] } = await request.json();
	return deleteSurveys(user_email, survey_codes);
};
