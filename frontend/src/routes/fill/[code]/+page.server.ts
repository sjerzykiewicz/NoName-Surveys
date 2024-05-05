import type { PageServerLoad } from './$types';
import * as db from '$lib/server/database';

export const load: PageServerLoad = async ({ params }) => {
	const survey_code = params.code;
	const { survey_structure } = await db.getSurveyByCode(survey_code);
	return survey_structure;
};
