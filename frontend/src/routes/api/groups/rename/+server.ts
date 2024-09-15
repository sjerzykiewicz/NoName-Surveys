import type { RequestHandler } from './$types';
import * as db from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const { user_email, name, new_name } = await request.json();
	return db.renameUserGroup(user_email, name, new_name);
};
