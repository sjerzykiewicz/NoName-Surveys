import type { RequestHandler } from './$types';
import { filterUnregisteredUsers } from '$lib/server/database';
import { getEmail } from '$lib/utils/getEmail';

export const POST: RequestHandler = async ({ request, cookies }) => {
	const sessionCookie = cookies.get('user_session');
	await getEmail(sessionCookie ?? '');
	const { emails } = await request.json();
	return filterUnregisteredUsers(emails);
};
