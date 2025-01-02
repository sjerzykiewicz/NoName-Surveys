import type { LayoutServerLoad } from './$types';
import { error, redirect } from '@sveltejs/kit';

export const load: LayoutServerLoad = async ({ parent, params, fetch }) => {
	const { session } = await parent();
	if (!session) {
		redirect(303, `/account`);
	}

	const page = parseInt(params.groupsPage);

	let retries = 2;
	while (retries > 0) {
		try {
			const [groupsResponse, usersResponse, countResponse] = await Promise.all([
				fetch(`/api/groups/all`, {
					method: 'POST',
					headers: {
						'Content-Type': 'application/json'
					},
					body: JSON.stringify({ page })
				}),
				fetch(`/api/users/all`),
				fetch(`/api/groups/count`)
			]);

			if (!groupsResponse.ok) {
				throw error(groupsResponse.status, { message: await groupsResponse.json() });
			}
			const group_list: {
				user_group_name: string;
				all_members_have_public_keys: true;
			}[] = await groupsResponse.json();

			if (!usersResponse.ok) {
				throw error(usersResponse.status, { message: await usersResponse.json() });
			}
			const user_list: string[] = await usersResponse.json();

			if (!countResponse.ok) {
				throw error(countResponse.status, { message: await countResponse.json() });
			}
			const numGroups: number = await countResponse.json();

			return {
				group_list,
				user_list,
				numGroups
			};
		} catch (err) {
			console.error(err);
			retries--;
			if (retries === 0) {
				throw error(500, { message: 'Failed to fetch data after multiple attempts' });
			}
		}
	}
};
