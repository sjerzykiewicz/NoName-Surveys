import type { PageServerLoad } from './$types';
import { getUserGroup, countUserGroupMembers } from '$lib/server/database';
import { error } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ parent, params }) => {
	const { session } = await parent();
	if (!session) {
		error(401, 'You must be logged in to access this page.');
	}

	const group = params.group;
	const page = parseInt(params.groupPage);

	const usersResponse = await getUserGroup(session.user!.email!, group, page);
	if (!usersResponse.ok) {
		error(usersResponse.status, { message: await usersResponse.json() });
	}
	const users: { email: string; has_public_key: boolean }[] = await usersResponse.json();

	const countResponse = await countUserGroupMembers(session.user!.email!, group);
	if (!countResponse.ok) {
		error(countResponse.status, { message: await countResponse.json() });
	}
	const numMembers = await countResponse.json();

	return { group, users, numMembers };
};
