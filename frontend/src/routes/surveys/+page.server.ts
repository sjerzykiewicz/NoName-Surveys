import type { PageServerLoad } from '../$types';
import * as db from '$lib/server/database';
import { redirect } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ parent }) => {
	const { session } = await parent();
	if (!session) {
		redirect(303, `/account`);
	}

	const survey_list = await db.getSurveysOfUser(session.user!.email!);
	return { session, survey_list };
};
