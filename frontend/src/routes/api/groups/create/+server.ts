import type { RequestHandler } from './$types';
import { createUserGroup } from '$lib/server/database';
import { getEmail } from '$lib/utils/getEmail';

export const POST: RequestHandler = async ({ request, cookies }) => {
	const sessionCookie = cookies.get('user_session');
	const user_email = await getEmail(sessionCookie ?? '');
	const {
		user_group_name,
		user_group_members
	}: { user_group_name: string; user_group_members: string[] } = await request.json();
	return createUserGroup(user_email, user_group_name, user_group_members);
};
