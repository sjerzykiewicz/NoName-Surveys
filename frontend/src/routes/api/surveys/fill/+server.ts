import type { SurveyAnswer } from '$lib/entities/surveys/SurveyAnswer';
import { type RequestHandler } from '@sveltejs/kit';
import { saveSurveyAnswer } from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const answer: SurveyAnswer = await request.json();
	return saveSurveyAnswer(answer);
};
