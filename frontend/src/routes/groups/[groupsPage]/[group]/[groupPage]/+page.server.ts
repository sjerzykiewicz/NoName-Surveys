import type { PageServerLoad } from './$types';
import { error } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ parent, params, fetch }) => {
	const { session } = await parent();
	if (!session) {
		error(401, 'You must be logged in to access this page.');
	}

	const group = params.group;
	const page = parseInt(params.groupPage);

	const membersResponse = await fetch(`/api/groups/members/all`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ name: group, page })
	});
	if (!membersResponse.ok) {
		error(membersResponse.status, { message: await membersResponse.json() });
	}
	const members: { email: string; has_public_key: boolean }[] = await membersResponse.json();

	let retries = 2;
	while (retries > 0) {
		try {
			const [notMembersResponse, countResponse] = await Promise.all([
				fetch(`/api/groups/members/all-not-members`, {
					method: 'POST',
					headers: {
						'Content-Type': 'application/json'
					},
					body: JSON.stringify({ name: group })
				}),
				fetch(`/api/groups/members/count`, {
					method: 'POST',
					headers: {
						'Content-Type': 'application/json'
					},
					body: JSON.stringify({ name: group })
				})
			]);

			if (!notMembersResponse.ok) {
				throw error(notMembersResponse.status, { message: await notMembersResponse.json() });
			}
			const notMembers: string[] = await notMembersResponse.json();

			if (!countResponse.ok) {
				throw error(countResponse.status, { message: await countResponse.json() });
			}
			const numMembers: number = await countResponse.json();

			return { group, members, notMembers, numMembers };
		} catch (err) {
			console.error(err);
			retries--;
			if (retries === 0) {
				throw error(500, { message: 'Failed to fetch data after multiple attempts' });
			}
		}
	}
};
