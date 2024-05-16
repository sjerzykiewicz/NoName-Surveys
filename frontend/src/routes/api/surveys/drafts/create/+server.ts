import type DraftCreateInfo from '$lib/entities/surveys/DraftCreateInfo';
import type { RequestHandler } from './$types';
import * as db from '$lib/server/database';
import { json } from '@sveltejs/kit';

export const POST: RequestHandler = async ({ request }) => {
	const info: DraftCreateInfo = await request.json();
	const response = await db.saveDraft(info);
	return json({ response });
};
