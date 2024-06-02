import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import * as db from '$lib/server/database';

export const load: PageServerLoad = async ({ parent }) => {
	const { session } = await parent();
	if (!session) {
		error(401, 'You must be logged in to access this page.');
	}

	const user_list: Array<string> = await db.getAllUsers();

	return { session, user_list };
};
