import type SurveyAnswer from '$lib/entities/surveys/SurveyAnswer';
import type { RequestHandler } from './$types';
import { saveSurveyAnswer } from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const answer: SurveyAnswer = await request.json();
	return saveSurveyAnswer(answer);
};
