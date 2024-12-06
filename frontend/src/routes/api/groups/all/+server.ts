import type { RequestHandler } from './$types';
import { getUserGroups } from '$lib/server/database';
import { getEmail } from '$lib/utils/getEmail';

export const POST: RequestHandler = async ({ request, cookies }) => {
	const sessionCookie = cookies.get('user_session');
	const user_email = await getEmail(sessionCookie ?? '');
	const { page }: { page: number } = await request.json();
	return getUserGroups(user_email, page);
};
