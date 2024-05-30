import * as db from '$lib/server/database';
import { error } from '@sveltejs/kit';
import type { PageServerLoad } from '../$types';

export const load: PageServerLoad = async ({ parent }) => {
	const { session } = await parent();
	if (!session) {
		error(403, 'You must be logged in to access this page.');
	}

	const userid = 1; // TODO = user id
	const drafts = await db.getDraftsOfUser(userid);
	return { session, drafts };
};
