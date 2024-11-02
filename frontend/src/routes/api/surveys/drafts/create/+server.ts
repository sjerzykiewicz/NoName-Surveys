import type DraftCreateInfo from '$lib/entities/surveys/DraftCreateInfo';
import type { RequestHandler } from './$types';
import { createSurveyDraft } from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const info: DraftCreateInfo = await request.json();
	return createSurveyDraft(info);
};
