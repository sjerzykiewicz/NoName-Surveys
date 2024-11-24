import type { RequestHandler } from './$types';
import { getWholeUserGroup } from '$lib/server/database';
import { getEmail } from '$lib/utils/getEmail';

export const POST: RequestHandler = async ({ request, cookies }) => {
	const sessionCookie = cookies.get('user_session');
	const user_email = await getEmail(sessionCookie ?? '');
	const { name } = await request.json();
	return getWholeUserGroup(user_email, name);
};
