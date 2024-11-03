import type { RequestHandler } from './$types';
import { createSurvey } from '$lib/server/database';
import type SurveyCreateInfo from '$lib/entities/surveys/SurveyCreateInfo';
import { getEmail } from '$lib/utils/getEmail';

export const POST: RequestHandler = async ({ request, cookies }) => {
	const sessionCookie = cookies.get('user_session');
	const user_email = await getEmail(sessionCookie ?? '');
	const info: SurveyCreateInfo = await request.json();
	info.user_email = user_email;
	return createSurvey(info);
};
