import type { RequestHandler } from './$types';
import { getUserGroup } from '$lib/server/database';
import { getEmail } from '$lib/utils/getEmail';

export const POST: RequestHandler = async ({ request, cookies }) => {
	const sessionCookie = cookies.get('user_session');
	const user_email = await getEmail(sessionCookie ?? '');
	const { name, page }: { name: string; page: number } = await request.json();
	return getUserGroup(user_email, name, page);
};
