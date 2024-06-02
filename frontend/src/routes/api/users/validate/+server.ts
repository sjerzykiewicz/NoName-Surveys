import type { RequestHandler } from '../../surveys/create/$types';
import * as db from '$lib/server/database';
import { json } from '@sveltejs/kit';

export const POST: RequestHandler = async ({ request }) => {
	const { email } = await request.json();
	const userHasPublicKey = await db.userHasPublicKey(email);
	return json(userHasPublicKey);
};
