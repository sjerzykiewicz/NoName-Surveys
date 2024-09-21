import type { RequestHandler } from './$types';
import * as db from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const { user_email, name } = await request.json();
	return db.deleteUserGroup(user_email, name);
};
