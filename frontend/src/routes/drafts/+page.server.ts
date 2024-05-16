import * as db from '$lib/server/database';
import type { PageServerLoad } from '../$types';

export const load: PageServerLoad = async () => {
	const userid = 1; // TODO = user id
	const drafts = await db.getDraftsOfUser(userid);
	return drafts;
};
