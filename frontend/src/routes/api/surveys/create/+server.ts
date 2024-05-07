import type { RequestHandler } from './$types';
import * as db from '$lib/server/database';
import { json } from '@sveltejs/kit';
import type SurveyCreateInfo from '$lib/entities/surveys/SurveyCreateInfo';

export const POST: RequestHandler = async ({ request }) => {
	const info: SurveyCreateInfo = await request.json();
	const { code } = await db.createSurvey(info);
	return json({ code });
};
