import type { PageServerLoad } from './$types';
import * as db from '$lib/server/database';
import { redirect } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ parent }) => {
	const { session } = await parent();
	if (!session) {
		redirect(303, `/account`);
	}

	const user_list: Array<string> = await db.getAllUsers();

	return { session, user_list };
};
