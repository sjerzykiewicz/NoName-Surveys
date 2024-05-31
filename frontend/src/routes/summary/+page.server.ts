import type { PageServerLoad } from '../$types';
import * as db from '$lib/server/database';
import { error } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ parent }) => {
	const { session } = await parent();
	if (!session) {
		error(403, 'You must be logged in to access this page.');
	}

	const survey_list = await db.getSurveysOfUser(session.user!.email!);
	return { session, survey_list };
};
