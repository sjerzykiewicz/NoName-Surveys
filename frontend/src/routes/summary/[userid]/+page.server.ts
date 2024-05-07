import type { PageServerLoad } from '../../$types';
import * as db from '$lib/server/database';

export const load: PageServerLoad = async ({ params }) => {
	const userid = params.userid;
	const survey_list = await db.getSurveysOfUser(userid);
	return { survey_list };
};
