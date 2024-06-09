import type { RequestHandler } from '../../surveys/create/$types';
import * as db from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const { email, public_key } = await request.json();

	return db.updatePublicKey(email, public_key);
};
