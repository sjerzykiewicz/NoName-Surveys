import type { PageServerLoad } from './$types';
import {
	getUserGroup,
	countUserGroupMembers,
	getAllUsersWhoAreNotMembers
} from '$lib/server/database';
import { error } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ parent, params }) => {
	const { session } = await parent();
	if (!session) {
		error(401, 'You must be logged in to access this page.');
	}

	const group = params.group;
	const page = parseInt(params.groupPage);

	const membersResponse = await getUserGroup(session.user!.email!, group, page);
	if (!membersResponse.ok) {
		error(membersResponse.status, { message: await membersResponse.json() });
	}
	const members: { email: string; has_public_key: boolean }[] = await membersResponse.json();

	const notMembersResponse = await getAllUsersWhoAreNotMembers(session.user!.email!, group);
	if (!notMembersResponse.ok) {
		error(notMembersResponse.status, { message: await notMembersResponse.json() });
	}
	const notMembers: string[] = await notMembersResponse.json();

	const countResponse = await countUserGroupMembers(session.user!.email!, group);
	if (!countResponse.ok) {
		error(countResponse.status, { message: await countResponse.json() });
	}
	const numMembers: number = await countResponse.json();

	return { group, members, notMembers, numMembers };
};
