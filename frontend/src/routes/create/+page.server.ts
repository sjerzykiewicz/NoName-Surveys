import type { PageServerLoad } from './$types';
import { getUserGroupsWithKeys, getUsersWithKeys } from '$lib/server/database';
import { error, redirect } from '@sveltejs/kit';
import { getEmail } from '$lib/utils/getEmail';

export const load: PageServerLoad = async ({ parent, cookies }) => {
	const { session } = await parent();
	if (!session) {
		redirect(303, `/account`);
	}

	const sessionCookie = cookies.get('user_session');
	const user_email = await getEmail(sessionCookie ?? '');

	const groupsResponse = await getUserGroupsWithKeys(user_email);
	if (!groupsResponse.ok) {
		error(groupsResponse.status, { message: await groupsResponse.json() });
	}
	const group_list: string[] = await groupsResponse.json();

	const usersResponse = await getUsersWithKeys();
	if (!usersResponse.ok) {
		error(usersResponse.status, { message: await usersResponse.json() });
	}
	const user_list: string[] = await usersResponse.json();

	return { group_list, user_list };
};
