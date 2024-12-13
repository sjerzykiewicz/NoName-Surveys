import type { RequestHandler } from './$types';
import { getUsersWithKeys } from '$lib/server/database';
import { getEmail } from '$lib/utils/getEmail';

export const GET: RequestHandler = async ({ cookies }) => {
	const sessionCookie = cookies.get('user_session');
	await getEmail(sessionCookie ?? '');
	return getUsersWithKeys();
};
