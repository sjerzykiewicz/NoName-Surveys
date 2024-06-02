import type { RequestHandler } from '../../surveys/create/$types';
import * as db from '$lib/server/database';
import { json } from '@sveltejs/kit';

export const POST: RequestHandler = async ({ request }) => {
	const { email, public_key } = await request.json();
	const isUserRegistered = await db.validateUser(email);
	if (isUserRegistered) {
		await db.updatePublicKey(email, public_key);
	}
	return json({ status: 200 });
};
