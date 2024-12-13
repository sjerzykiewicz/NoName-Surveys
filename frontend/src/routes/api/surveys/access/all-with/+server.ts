import type { RequestHandler } from './$types';
import { checkAccessToSurvey } from '$lib/server/database';
import { getEmail } from '$lib/utils/getEmail';

export const POST: RequestHandler = async ({ request, cookies }) => {
	const sessionCookie = cookies.get('user_session');
	const user_email = await getEmail(sessionCookie ?? '');
	const { survey_code, page }: { survey_code: string; page: number } = await request.json();
	return checkAccessToSurvey(user_email, survey_code, page);
};
