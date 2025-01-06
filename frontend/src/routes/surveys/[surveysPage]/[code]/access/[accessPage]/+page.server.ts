import type { PageServerLoad } from './$types';
import { error } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ params, fetch }) => {
	const code = params.code;
	const page = parseInt(params.accessPage);

	const response = await fetch(`/api/combined/surveys_access`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ survey_code: code, page })
	});

	if (!response.ok) {
		throw error(response.status, { message: await response.json() });
	}

	const { has_access, without_access, users_count } = await response.json();

	return {
		usersWithAccess: has_access,
		usersWithoutAccess: without_access,
		numUsers: users_count
	};
};
