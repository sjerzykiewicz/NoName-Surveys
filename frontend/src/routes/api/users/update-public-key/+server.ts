import type { RequestHandler } from './$types';
import * as db from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const { email, public_key, fingerprint } = await request.json();

	return db.updatePublicKey(email, public_key, fingerprint);
};
