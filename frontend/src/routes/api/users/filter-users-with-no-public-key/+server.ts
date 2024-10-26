import type { RequestHandler } from './$types';
import * as db from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const { emails } = await request.json();
	return db.filterUsersWithNoPublicKey(emails);
};
