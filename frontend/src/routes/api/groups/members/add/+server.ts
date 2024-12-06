import type { RequestHandler } from './$types';
import { addUsersToGroup } from '$lib/server/database';
import { getEmail } from '$lib/utils/getEmail';

export const POST: RequestHandler = async ({ request, cookies }) => {
	const sessionCookie = cookies.get('user_session');
	const user_email = await getEmail(sessionCookie ?? '');
	const { name, users }: { name: string; users: string[] } = await request.json();
	return addUsersToGroup(user_email, name, users);
};