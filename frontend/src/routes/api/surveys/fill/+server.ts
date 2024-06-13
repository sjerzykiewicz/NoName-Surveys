import type { SurveyAnswer } from '$lib/entities/surveys/SurveyAnswer';
import { type RequestHandler } from '@sveltejs/kit';
import * as db from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const answer: SurveyAnswer = await request.json();
	return db.saveAnswer(answer);
};
