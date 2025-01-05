import type { RequestHandler } from './$types';
import {
	countSurveys,
	countSurveyDrafts,
	getUsersWithKeys,
	getUserGroupsWithKeys
} from '$lib/server/database';
import { getEmail } from '$lib/utils/getEmail';
import { error } from '@sveltejs/kit';

export const GET: RequestHandler = async ({ cookies }) => {
	const sessionCookie = cookies.get('user_session');
	const user_email = await getEmail(sessionCookie ?? '');
	if (!user_email) {
		return error(500, {
			message: 'Failed to get data from the USOS API. Please try reloading the page'
		});
	}

	const [groups, users, drafts_count, surveys_count] = await Promise.all([
		getUserGroupsWithKeys(user_email),
		getUsersWithKeys(),
		countSurveyDrafts(user_email),
		countSurveys(user_email)
	]);

	const responseBody = {
		groups: await groups.json(),
		users: await users.json(),
		drafts_count: await drafts_count.json(),
		surveys_count: await surveys_count.json()
	};

	return new Response(JSON.stringify(responseBody), {
		status: 200,
		headers: {
			'Content-Type': 'application/json'
		}
	});
};
