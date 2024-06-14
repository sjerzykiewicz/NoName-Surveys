import type { LayoutServerLoad } from './$types';
import * as db from '$lib/server/database';
import { error } from '@sveltejs/kit';

export const load: LayoutServerLoad = async ({ params, parent }) => {
	const { session } = await parent();
	if (!session) {
		error(401, 'You must be logged in to access this page.');
	}
	const code = params.code;
	const surveyResponse = await db.getSurveyByCode(code);
	if (!surveyResponse.ok) {
		error(surveyResponse.status, { message: await surveyResponse.json() });
	}
	const answersResponse = await db.getSurveyAnswers(session.user!.email!, code);
	if (!answersResponse.ok) {
		error(answersResponse.status, { message: await answersResponse.json() });
	}

	const survey = await surveyResponse.json();
	const answers = await answersResponse.json();
	return { survey, answers, code };
};
