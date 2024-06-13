import type { RequestHandler } from './$types';
import * as db from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const { user_email, id } = await request.json();
	return db.getDraftStructureById(user_email, id);
};
