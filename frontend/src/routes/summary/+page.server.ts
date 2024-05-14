import type { PageServerLoad } from '../$types';
import * as db from '$lib/server/database';

export const load: PageServerLoad = async () => {
	const userid = 1; // TODO = user id
	const survey_list = await db.getSurveysOfUser(userid);
	return { survey_list };
};
