import type { RequestHandler } from './$types';
import { getSurveyRespondents } from '$lib/server/database';
import { getEmail } from '$lib/utils/getEmail';

export const POST: RequestHandler = async ({ request, cookies }) => {
	const sessionCookie = cookies.get('user_session');
	await getEmail(sessionCookie ?? '');
	const { survey_code, page }: { survey_code: string; page: number } = await request.json();
	return getSurveyRespondents(survey_code, page);
};
