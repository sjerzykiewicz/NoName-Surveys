import type { RequestHandler } from './$types';
import { filterUsersWithNoPublicKey } from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const { emails } = await request.json();
	return filterUsersWithNoPublicKey(emails);
};
