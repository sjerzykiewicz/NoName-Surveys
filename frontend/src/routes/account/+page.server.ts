import type { PageServerLoad } from './$types';
import { getKeyCreationDate } from '$lib/server/database';
import { getEmail } from '$lib/utils/getEmail';

export const load: PageServerLoad = async ({ parent, cookies }) => {
	const { session } = await parent();
	let key_creation_date: string | null = null;
	if (session?.user.email) {
		const sessionCookie = cookies.get('user_session');
		const user_email = await getEmail(sessionCookie ?? '');
		const response = await getKeyCreationDate(user_email);
		key_creation_date = await response.json();
	}
	return { session, key_creation_date };
};
