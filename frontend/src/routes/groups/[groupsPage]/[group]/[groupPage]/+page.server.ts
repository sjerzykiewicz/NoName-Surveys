import type { PageServerLoad } from './$types';
import {
	getUserGroup,
	countUserGroupMembers,
	getAllUsersWhoAreNotMembers
} from '$lib/server/database';
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

	const membersResponse = await getUserGroup(user_email, group, page);
	if (!membersResponse.ok) {
		error(membersResponse.status, { message: await membersResponse.json() });
	}
	const members: { email: string; has_public_key: boolean }[] = await membersResponse.json();

	const notMembersResponse = await getAllUsersWhoAreNotMembers(user_email, group);
	if (!notMembersResponse.ok) {
		error(notMembersResponse.status, { message: await notMembersResponse.json() });
	}
	const notMembers: string[] = await notMembersResponse.json();

	const countResponse = await countUserGroupMembers(user_email, group);
	if (!countResponse.ok) {
		error(countResponse.status, { message: await countResponse.json() });
	}
	const numMembers: number = await countResponse.json();

	return { group, members, notMembers, numMembers };
};
