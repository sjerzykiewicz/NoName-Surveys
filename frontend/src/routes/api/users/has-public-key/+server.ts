import type { RequestHandler } from './$types';
import { hasPublicKey } from '$lib/server/database';

export const POST: RequestHandler = async ({ request }) => {
	const { email } = await request.json();
	return hasPublicKey(email);
};
