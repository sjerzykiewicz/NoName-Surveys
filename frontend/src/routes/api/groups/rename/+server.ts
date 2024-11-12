import type { RequestHandler } from './$types';
import { renameUserGroup } from '$lib/server/database';
import { getEmail } from '$lib/utils/getEmail';

export const POST: RequestHandler = async ({ request, cookies }) => {
	const sessionCookie = cookies.get('user_session');
	const user_email = await getEmail(sessionCookie ?? '');
	const { name, new_name } = await request.json();
	return renameUserGroup(user_email, name, new_name);
};
