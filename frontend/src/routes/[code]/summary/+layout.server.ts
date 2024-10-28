import type { LayoutServerLoad } from './$types';
import { getSurvey, getSurveyAnswers, getSurveyRespondents } from '$lib/server/database';
import { error } from '@sveltejs/kit';

export const load: LayoutServerLoad = async ({ params, parent }) => {
	const { session } = await parent();
	if (!session) {
		error(401, 'You must be logged in to access this page.');
	}
	const code = params.code;
	const surveyResponse = await getSurvey(code);
	if (!surveyResponse.ok) {
		error(surveyResponse.status, { message: await surveyResponse.json() });
	}
	const answersResponse = await getSurveyAnswers(session.user!.email!, code);
	if (!answersResponse.ok) {
		error(answersResponse.status, { message: await answersResponse.json() });
	}
	const respondentsResponse = await getSurveyRespondents(code);
	if (!respondentsResponse.ok) {
		error(respondentsResponse.status, { message: await respondentsResponse.json() });
	}

	const survey = await surveyResponse.json();
	const answers = await answersResponse.json();
	const respondents = await respondentsResponse.json();
	return { survey, answers, respondents, code };
};
