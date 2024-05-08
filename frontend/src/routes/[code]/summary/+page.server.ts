import type { PageServerLoad } from './$types';
import * as db from '$lib/server/database';

export const load: PageServerLoad = async ({ params }) => {
	const code = params.code;
	const survey = await db.getSurveyByCode(code);
	const answers = await db.getSurveyAnswers(code);
	return { survey, answers, code };
};
