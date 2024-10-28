import type { RequestHandler } from './$types';
import { createUserGroup } from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const { user_email, user_group_name, user_group_members } = await request.json();
	return createUserGroup(user_email, user_group_name, user_group_members);
};
