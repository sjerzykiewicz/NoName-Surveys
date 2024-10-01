import type { RequestHandler } from './$types';
import * as db from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const { user_email } = await request.json();
	return db.getDraftsOfUser(user_email);
};
