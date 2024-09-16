import type { PageServerLoad } from '../$types';
import * as db from '$lib/server/database';
import { error, redirect } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ parent }) => {
	const { session } = await parent();
	if (!session) {
		redirect(303, `/account`);
	}

	const groupsResponse = await db.getAllUserGroups(session.user!.email!);
	if (!groupsResponse.ok) {
		error(groupsResponse.status, { message: await groupsResponse.json() });
	}
	const group_list = await groupsResponse.json();

	const usersResponse = await db.getAllUsers();
	if (!usersResponse.ok) {
		error(usersResponse.status, { message: await usersResponse.json() });
	}
	const user_list = await usersResponse.json();

	return { session, group_list, user_list };
};
