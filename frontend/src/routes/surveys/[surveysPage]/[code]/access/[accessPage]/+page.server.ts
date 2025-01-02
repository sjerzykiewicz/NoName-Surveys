import type { PageServerLoad } from './$types';
import { error } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ params, fetch }) => {
	const code = params.code;
	const page = parseInt(params.accessPage);

	const accessResponse = await fetch(`/api/surveys/access/all-with`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ survey_code: code, page })
	});
	if (!accessResponse.ok) {
		error(accessResponse.status, { message: await accessResponse.json() });
	}
	const usersWithAccess: string[] = await accessResponse.json();

	const notAccessResponse = await fetch(`/api/surveys/access/all-without`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ survey_code: code })
	});
	if (!notAccessResponse.ok) {
		error(notAccessResponse.status, { message: await notAccessResponse.json() });
	}
	const usersWithoutAccess: string[] = await notAccessResponse.json();

	const countResponse = await fetch(`/api/surveys/access/count`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ survey_code: code })
	});
	if (!countResponse.ok) {
		error(countResponse.status, { message: await countResponse.json() });
	}
	const numUsers: number = await countResponse.json();

	return { usersWithAccess, usersWithoutAccess, numUsers };
};
