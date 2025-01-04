import type { RequestHandler } from './$types';
import {
	checkAccessToSurvey,
	getAllUsersWithoutAccess,
	countUsersWithAccess
} from '$lib/server/database';
import { getEmail } from '$lib/utils/getEmail';
import { error } from '@sveltejs/kit';

export const POST: RequestHandler = async ({ request, cookies }) => {
	const sessionCookie = cookies.get('user_session');
	const { survey_code, page }: { survey_code: string; page: number } = await request.json();
	const user_email = await getEmail(sessionCookie ?? '');
	if (!user_email) {
		return error(500, { message: 'Failed to get data from USOS' });
	}

	const [has_access, without_access, users_count] = await Promise.all([
		checkAccessToSurvey(user_email, survey_code, page),
		getAllUsersWithoutAccess(user_email, survey_code),
		countUsersWithAccess(user_email, survey_code)
	]);

	const responseBody = {
		has_access: await has_access.json(),
		without_access: await without_access.json(),
		users_count: await users_count.json()
	};

	return new Response(JSON.stringify(responseBody), {
		status: 200,
		headers: {
			'Content-Type': 'application/json'
		}
	});
};
