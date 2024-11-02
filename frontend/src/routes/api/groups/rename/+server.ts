import type { RequestHandler } from './$types';
import { renameUserGroup } from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const { user_email, name, new_name } = await request.json();
	return renameUserGroup(user_email, name, new_name);
};
