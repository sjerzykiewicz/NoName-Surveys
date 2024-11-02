import type { RequestHandler } from './$types';
import { deleteUserGroup } from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const { user_email, name } = await request.json();
	return deleteUserGroup(user_email, name);
};
