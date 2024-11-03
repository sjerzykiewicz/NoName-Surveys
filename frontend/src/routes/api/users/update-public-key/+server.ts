import type { RequestHandler } from '../../surveys/create/$types';
import * as db from '$lib/server/database';
import { getEmail } from '$lib/utils/getEmail';

export const POST: RequestHandler = async ({ request, cookies }) => {
	const sessionCookie = cookies.get('user_session');
	const user_email = await getEmail(sessionCookie ?? '');
	const { public_key, fingerprint } = await request.json();

	return db.updatePublicKey(user_email, public_key, fingerprint);
};
