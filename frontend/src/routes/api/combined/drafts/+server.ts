import type { RequestHandler } from './$types';
import {
	getSurveyDrafts,
	countSurveys,
	countSurveyDrafts,
	getUsersWithKeys,
	getUserGroupsWithKeys
} from '$lib/server/database';
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

	const [drafts, groups, users, drafts_count, surveys_count] = await Promise.all([
		getSurveyDrafts(user_email, page),
		getUserGroupsWithKeys(user_email),
		getUsersWithKeys(),
		countSurveyDrafts(user_email),
		countSurveys(user_email)
	]);

	const responseBody = {
		drafts: await drafts.json(),
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
