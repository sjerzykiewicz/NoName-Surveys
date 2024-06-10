import type { LayoutServerLoad } from './$types';
import * as db from '$lib/server/database';
import { error } from '@sveltejs/kit';
import { responseErrorHandler } from '$lib/utils/responseErrorHandler';

export const load: LayoutServerLoad = async ({ params, parent }) => {
	const { session } = await parent();
	if (!session) {
		error(401, 'You must be logged in to access this page.');
	}
	const code = params.code;
	const surveyResponse = await db.getSurveyByCode(code);
	if (!surveyResponse.ok) {
		responseErrorHandler(surveyResponse);
	}
	const answersResponse = await db.getSurveyAnswers(session.user!.email!, code);
	if (!answersResponse.ok) {
		responseErrorHandler(answersResponse);
	}

	const survey = await surveyResponse.json();
	const answers = await answersResponse.json();
	return { survey, answers, code };
};
