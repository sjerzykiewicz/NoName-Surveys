import type { RequestHandler } from './$types';
import { getUserGroup } from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const { user_email, name } = await request.json();
	return getUserGroup(user_email, name);
};
