import type { LayoutServerLoad } from './$types';
import { error, redirect } from '@sveltejs/kit';

export const load: LayoutServerLoad = async ({ parent, params, fetch }) => {
	const { session } = await parent();
	if (!session) {
		redirect(303, `/account`);
	}

	const page = parseInt(params.groupsPage);

	const response = await fetch(`/api/combined/groups_users`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ page })
	});

	if (!response.ok) {
		throw error(response.status, { message: await response.json() });
	}

	const { groups, groups_count, users } = await response.json();

	return {
		group_list: groups,
		user_list: users,
		numGroups: groups_count
	};
};
