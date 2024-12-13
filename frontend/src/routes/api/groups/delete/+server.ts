import type { RequestHandler } from './$types';
import { deleteUserGroups } from '$lib/server/database';
import { getEmail } from '$lib/utils/getEmail';

export const POST: RequestHandler = async ({ request, cookies }) => {
	const sessionCookie = cookies.get('user_session');
	const user_email = await getEmail(sessionCookie ?? '');
	const { names }: { names: string[] } = await request.json();
	return deleteUserGroups(user_email, names);
};
