import type { LayoutServerLoad } from './$types';
import { getUserGroups, getUsers, countUserGroups } from '$lib/server/database';
import { error, redirect } from '@sveltejs/kit';
import { getEmail } from '$lib/utils/getEmail';

export const load: LayoutServerLoad = async ({ parent, params, cookies }) => {
	const { session } = await parent();
	if (!session) {
		redirect(303, `/account`);
	}

	const page = parseInt(params.groupsPage);

	const sessionCookie = cookies.get('user_session');
	const user_email = await getEmail(sessionCookie ?? '');

	const groupsResponse = await getUserGroups(user_email, page);
	if (!groupsResponse.ok) {
		error(groupsResponse.status, { message: await groupsResponse.json() });
	}
	const group_list: {
		user_group_name: string;
		all_members_have_public_keys: true;
	}[] = await groupsResponse.json();

	const usersResponse = await getUsers();
	if (!usersResponse.ok) {
		error(usersResponse.status, { message: await usersResponse.json() });
	}
	const user_list: string[] = await usersResponse.json();

	const countResponse = await countUserGroups(user_email);
	if (!countResponse.ok) {
		error(countResponse.status, { message: await countResponse.json() });
	}
	const numGroups: number = await countResponse.json();

	return { session, group_list, user_list, numGroups };
};
