import type { PageServerLoad } from './$types';
import { checkAccessToSurvey, getUsers } from '$lib/server/database';
import { error } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ params, parent }) => {
	const { session } = await parent();
	if (!session) {
		error(401, 'You must be logged in to access this page.');
	}

	const accessResponse = await checkAccessToSurvey(session.user!.email!, params.code);
	if (!accessResponse.ok) {
		error(accessResponse.status, { message: await accessResponse.json() });
	}

	const usersResponse = await getUsers();
	if (!usersResponse.ok) {
		error(usersResponse.status, { message: await usersResponse.json() });
	}

	const usersWithAccess = await accessResponse.json();
	const allUsers = await usersResponse.json();

	return { usersWithAccess, allUsers };
};
