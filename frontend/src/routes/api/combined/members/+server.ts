import type { RequestHandler } from './$types';
import {
	getUserGroup,
	getAllUsersWhoAreNotMembers,
	countUserGroupMembers
} from '$lib/server/database';
import { getEmail } from '$lib/utils/getEmail';
import { error } from '@sveltejs/kit';

export const POST: RequestHandler = async ({ request, cookies }) => {
	const sessionCookie = cookies.get('user_session');
	const { group, page }: { group: string; page: number } = await request.json();
	const user_email = await getEmail(sessionCookie ?? '');
	if (!user_email) {
		return error(500, {
			message: 'Failed to get data from the USOS API. Please try reloading the page'
		});
	}

	const [members, notMembers, count] = await Promise.all([
		getUserGroup(user_email, group, page),
		getAllUsersWhoAreNotMembers(user_email, group),
		countUserGroupMembers(user_email, group)
	]);

	const responseBody = {
		members: await members.json(),
		notMembers: await notMembers.json(),
		count: await count.json()
	};

	return new Response(JSON.stringify(responseBody), {
		status: 200,
		headers: {
			'Content-Type': 'application/json'
		}
	});
};
