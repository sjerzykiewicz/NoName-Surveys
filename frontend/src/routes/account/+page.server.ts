import type { PageServerLoad } from './$types';
import { hasPublicKey, getKeyCreationDate } from '$lib/server/database';
import { error } from '@sveltejs/kit';
import { getEmail } from '$lib/utils/getEmail';

export const load: PageServerLoad = async ({ parent, cookies }) => {
	const { session } = await parent();
	if (!session) {
		return { session, hasKey: false, keyCreationDate: '' };
	}

	const sessionCookie = cookies.get('user_session');
	const user_email = await getEmail(sessionCookie ?? '');

	const keyResponse = await hasPublicKey(user_email);
	if (!keyResponse.ok) {
		error(keyResponse.status, { message: await keyResponse.json() });
	}
	const hasKey: boolean = await keyResponse.json();

	const dateResponse = await getKeyCreationDate(user_email);
	if (!dateResponse.ok) {
		error(dateResponse.status, { message: await dateResponse.json() });
	}
	const keyCreationDate: string = await dateResponse.json();

	return { session, hasKey, keyCreationDate };
};
