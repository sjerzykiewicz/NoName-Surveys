import type { RequestHandler } from './$types';
import { getUserGroups } from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const { user_email } = await request.json();
	return getUserGroups(user_email);
};
