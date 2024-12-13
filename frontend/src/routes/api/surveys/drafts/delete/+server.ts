import type { RequestHandler } from './$types';
import { deleteSurveyDrafts } from '$lib/server/database';
import { getEmail } from '$lib/utils/getEmail';

export const POST: RequestHandler = async ({ request, cookies }) => {
	const sessionCookie = cookies.get('user_session');
	const user_email = await getEmail(sessionCookie ?? '');
	const { ids }: { ids: number[] } = await request.json();
	return deleteSurveyDrafts(user_email, ids);
};
