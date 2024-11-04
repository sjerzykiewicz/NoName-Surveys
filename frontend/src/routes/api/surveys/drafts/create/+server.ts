import type DraftCreateInfo from '$lib/entities/surveys/DraftCreateInfo';
import type { RequestHandler } from './$types';
import { createSurveyDraft } from '$lib/server/database';
import { getEmail } from '$lib/utils/getEmail';

export const POST: RequestHandler = async ({ request, cookies }) => {
	const sessionCookie = cookies.get('user_session');
	const user_email = await getEmail(sessionCookie ?? '');
	const info: DraftCreateInfo = await request.json();
	info.user_email = user_email;
	return createSurveyDraft(info);
};
