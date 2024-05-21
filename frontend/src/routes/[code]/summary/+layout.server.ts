import type { LayoutServerLoad } from './$types';
import * as db from '$lib/server/database';

export const load: LayoutServerLoad = async ({ params }) => {
	const code = params.code;
	const survey = await db.getSurveyByCode(code);
	const answers = await db.getSurveyAnswers(code);
	return { survey, answers, code };
};
