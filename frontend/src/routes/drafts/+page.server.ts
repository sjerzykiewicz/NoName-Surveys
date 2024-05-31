import * as db from '$lib/server/database';
import { error } from '@sveltejs/kit';
import type { PageServerLoad } from '../$types';

export const load: PageServerLoad = async ({ parent }) => {
	const { session } = await parent();
	if (!session) {
		error(403, 'You must be logged in to access this page.');
	}

	const drafts = await db.getDraftsOfUser(session.user!.email!);
	return { session, drafts };
};
