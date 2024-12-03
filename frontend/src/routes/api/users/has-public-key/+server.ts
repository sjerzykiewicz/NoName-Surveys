import type { RequestHandler } from './$types';
import { hasPublicKey } from '$lib/server/database';
import { getEmail } from '$lib/utils/getEmail';

export const GET: RequestHandler = async ({ cookies }) => {
	const sessionCookie = cookies.get('user_session');
	console.log('sessionCookie:', sessionCookie);
	const user_email = await getEmail(sessionCookie ?? '');
	console.log('user_email:', user_email);
	return hasPublicKey(user_email);
};
