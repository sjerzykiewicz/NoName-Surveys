import type { PageServerLoad } from '../$types';
import { getUserGroups, getUsers } from '$lib/server/database';
import { error, redirect } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ parent }) => {
	const { session } = await parent();
	if (!session) {
		redirect(303, `/account`);
	}

	const groupsResponse = await getUserGroups(session.user!.email!);
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

	return { session, group_list, user_list };
};
