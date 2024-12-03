import type { LayoutServerLoad } from './$types';
import { error, redirect } from '@sveltejs/kit';

export const load: LayoutServerLoad = async ({ parent, params, url }) => {
	const { session } = await parent();
	if (!session) {
		redirect(303, `/account`);
	}

	const page = parseInt(params.groupsPage);
	const host = url.origin;

	const groupsResponse = await fetch(`${host}/api/groups/all`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ page })
	});
	if (!groupsResponse.ok) {
		error(groupsResponse.status, { message: await groupsResponse.json() });
	}
	const group_list: {
		user_group_name: string;
		all_members_have_public_keys: true;
	}[] = await groupsResponse.json();

	const usersResponse = await fetch(`${host}/api/users/all`);
	if (!usersResponse.ok) {
		error(usersResponse.status, { message: await usersResponse.json() });
	}
	const user_list: string[] = await usersResponse.json();

	const countResponse = await fetch(`${host}/api/groups/count`);
	if (!countResponse.ok) {
		error(countResponse.status, { message: await countResponse.json() });
	}
	const numGroups: number = await countResponse.json();

	return { session, group_list, user_list, numGroups };
};
