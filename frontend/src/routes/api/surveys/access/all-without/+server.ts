import type { RequestHandler } from './$types';
import { getAllUsersWithoutAccess } from '$lib/server/database';
import { getEmail } from '$lib/utils/getEmail';

export const POST: RequestHandler = async ({ request, cookies }) => {
	const sessionCookie = cookies.get('user_session');
	const user_email = await getEmail(sessionCookie ?? '');
	const { survey_code }: { survey_code: string } = await request.json();
	return getAllUsersWithoutAccess(user_email, survey_code);
};
