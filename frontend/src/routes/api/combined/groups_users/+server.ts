import type { RequestHandler } from './$types';
import { getUserGroups, countUserGroups, getUsers } from '$lib/server/database';
import { getEmail } from '$lib/utils/getEmail';
import { error } from '@sveltejs/kit';

export const POST: RequestHandler = async ({ request, cookies }) => {
	const sessionCookie = cookies.get('user_session');
	const { page }: { page: number } = await request.json();
	const user_email = await getEmail(sessionCookie ?? '');
	if (!user_email) {
		return error(500, {
			message: 'Failed to get data from the USOS API. Please try reloading the page'
		});
	}

	const [groups, groups_count, users] = await Promise.all([
		getUserGroups(user_email, page),
		countUserGroups(user_email),
		getUsers()
	]);

	const responseBody = {
		groups: await groups.json(),
		groups_count: await groups_count.json(),
		users: await users.json()
	};

	return new Response(JSON.stringify(responseBody), {
		status: 200,
		headers: {
			'Content-Type': 'application/json'
		}
	});
};
