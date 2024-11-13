import type { PageServerLoad } from './$types';
import { getUserGroup, countUserGroupMembers } from '$lib/server/database';
import { error } from '@sveltejs/kit';
import { getEmail } from '$lib/utils/getEmail';

export const load: PageServerLoad = async ({ parent, params, cookies }) => {
	const { session } = await parent();
	if (!session) {
		error(401, 'You must be logged in to access this page.');
	}

	const group = params.group;
	const page = parseInt(params.groupPage);

	const sessionCookie = cookies.get('user_session');
	const user_email = await getEmail(sessionCookie ?? '');

	const usersResponse = await getUserGroup(user_email, group, page);
	if (!usersResponse.ok) {
		error(usersResponse.status, { message: await usersResponse.json() });
	}
	const users: { email: string; has_public_key: boolean }[] = await usersResponse.json();

	const countResponse = await countUserGroupMembers(user_email, group);
	if (!countResponse.ok) {
		error(countResponse.status, { message: await countResponse.json() });
	}
	const numMembers = await countResponse.json();

	return { group, users, numMembers };
};
