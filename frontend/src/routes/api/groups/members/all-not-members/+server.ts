import type { RequestHandler } from './$types';
import { getAllUsersWhoAreNotMembers } from '$lib/server/database';
import { getEmail } from '$lib/utils/getEmail';

export const POST: RequestHandler = async ({ request, cookies }) => {
	const sessionCookie = cookies.get('user_session');
	const user_email = await getEmail(sessionCookie ?? '');
	const { name }: { name: string } = await request.json();
	return getAllUsersWhoAreNotMembers(user_email, name);
};
