import type { RequestHandler } from './$types';
import { getSurveys, countSurveys } from '$lib/server/database';
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

	const [surveys, count] = await Promise.all([
		getSurveys(user_email, page),
		countSurveys(user_email)
	]);

	const responseBody = {
		surveys: await surveys.json(),
		count: await count.json()
	};

	return new Response(JSON.stringify(responseBody), {
		status: 200,
		headers: {
			'Content-Type': 'application/json'
		}
	});
};
