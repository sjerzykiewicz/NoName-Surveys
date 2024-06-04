import * as db from '$lib/server/database';
import type { PageServerLoad } from '../$types';
import { redirect } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ parent }) => {
	const { session } = await parent();
	if (!session) {
		redirect(303, `/account`);
	}

	const drafts = await db.getDraftsOfUser(session.user!.email!);
	return { session, drafts };
};
