import type { LayoutServerLoad } from './$types';
import * as db from '$lib/server/database';
import { error } from '@sveltejs/kit';

export const load: LayoutServerLoad = async ({ params, parent }) => {
	const { session } = await parent();
	if (!session) {
		error(403, 'You must be logged in to access this page.');
	}
	const code = params.code;
	const survey = await db.getSurveyByCode(code);
	const answers = await db.getSurveyAnswers(session.user!.email!, code);
	return { survey, answers, code };
};
