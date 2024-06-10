import type { RequestHandler } from '../../surveys/create/$types';
import * as db from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const { email } = await request.json();
	return db.userHasPublicKey(email);
};
