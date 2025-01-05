import type { RequestHandler } from './$types';
import { countSurveyRespondents } from '$lib/server/database';
import { getEmail } from '$lib/utils/getEmail';

export const POST: RequestHandler = async ({ request, cookies }) => {
	const sessionCookie = cookies.get('user_session');
	await getEmail(sessionCookie ?? '');
	const { survey_code }: { survey_code: string } = await request.json();
	return countSurveyRespondents(survey_code);
};
