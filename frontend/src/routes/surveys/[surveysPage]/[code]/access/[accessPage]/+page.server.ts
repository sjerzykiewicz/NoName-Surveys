import type { PageServerLoad } from './$types';
import { error } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ parent, params, fetch }) => {
	const { session } = await parent();
	if (!session) {
		error(401, 'You must be logged in to access this page.');
	}

	const code = params.code;
	const page = parseInt(params.accessPage);

	try {
		const [accessResponse, notAccessResponse, countResponse] = await Promise.all([
			fetch(`/api/surveys/access/all-with`, {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({ survey_code: code, page })
			}),
			fetch(`/api/surveys/access/all-without`, {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({ survey_code: code })
			}),
			fetch(`/api/surveys/access/count`, {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({ survey_code: code })
			})
		]);

		if (!accessResponse.ok) {
			throw error(accessResponse.status, { message: await accessResponse.json() });
		}
		const usersWithAccess: string[] = await accessResponse.json();

		if (!notAccessResponse.ok) {
			throw error(notAccessResponse.status, { message: await notAccessResponse.json() });
		}
		const usersWithoutAccess: string[] = await notAccessResponse.json();

		if (!countResponse.ok) {
			throw error(countResponse.status, { message: await countResponse.json() });
		}
		const numUsers: number = await countResponse.json();

		return { usersWithAccess, usersWithoutAccess, numUsers };
	} catch (err) {
		console.error(err);
		throw error(500, { message: 'Failed to fetch data' });
	}
};
