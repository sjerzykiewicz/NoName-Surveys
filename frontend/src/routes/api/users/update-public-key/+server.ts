import type { RequestHandler } from './$types';
import { updatePublicKey } from '$lib/server/database';
import { getEmail } from '$lib/utils/getEmail';

export const POST: RequestHandler = async ({ request, cookies }) => {
	const sessionCookie = cookies.get('user_session');
	const user_email = await getEmail(sessionCookie ?? '');
	const { public_key, fingerprint }: { public_key: string; fingerprint: string } =
		await request.json();
	return updatePublicKey(user_email, public_key, fingerprint);
};
