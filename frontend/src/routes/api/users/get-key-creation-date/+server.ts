import type { RequestHandler } from './$types';
import { getKeyCreationDate } from '$lib/server/database';
import { getEmail } from '$lib/utils/getEmail';

export const GET: RequestHandler = async ({ cookies }) => {
	const sessionCookie = cookies.get('user_session');
	const user_email = await getEmail(sessionCookie ?? '');
	return getKeyCreationDate(user_email);
};
