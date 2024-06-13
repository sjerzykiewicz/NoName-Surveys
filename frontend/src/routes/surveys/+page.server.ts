import type { PageServerLoad } from '../$types';
import * as db from '$lib/server/database';
import { redirect } from '@sveltejs/kit';
import { responseErrorHandler } from '$lib/utils/responseErrorHandler';

export const load: PageServerLoad = async ({ parent }) => {
	const { session } = await parent();
	if (!session) {
		redirect(303, `/account`);
	}

	const response = await db.getSurveysOfUser(session.user!.email!);
	if (!response.ok) {
		responseErrorHandler(response);
	}
	const survey_list = await response.json();
	return { session, survey_list };
};
