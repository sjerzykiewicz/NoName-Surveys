import type { RequestHandler } from './$types';
import { getSurvey } from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const { survey_code }: { survey_code: string } = await request.json();
	return getSurvey(survey_code);
};
