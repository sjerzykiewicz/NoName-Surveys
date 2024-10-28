import type { RequestHandler } from './$types';
import { updatePublicKey } from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const { email, public_key, fingerprint } = await request.json();
	return updatePublicKey(email, public_key, fingerprint);
};
