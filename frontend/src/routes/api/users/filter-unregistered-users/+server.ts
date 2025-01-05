import type { RequestHandler } from './$types';
import { filterUnregisteredUsers } from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const { emails } = await request.json();
	return filterUnregisteredUsers(emails);
};
