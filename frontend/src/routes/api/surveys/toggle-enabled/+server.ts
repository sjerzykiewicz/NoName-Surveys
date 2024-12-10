import type { RequestHandler } from './$types';
import { enableOrDisableSurvey } from '$lib/server/database';
import { getEmail } from '$lib/utils/getEmail';

export const POST: RequestHandler = async ({ request, cookies }) => {
	const sessionCookie = cookies.get('user_session');
	const user_email = await getEmail(sessionCookie ?? '');
	const { survey_code, is_enabled }: { survey_code: string; is_enabled: boolean } =
		await request.json();
	return enableOrDisableSurvey(user_email, survey_code, is_enabled);
};
