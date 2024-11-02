import type { PageServerLoad } from './$types';
import { checkAccessToSurvey, getUsers } from '$lib/server/database';
import { error } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ parent, params }) => {
	const { session } = await parent();

	const code = params.code;
	const page = parseInt(params.page);

	const accessResponse = await checkAccessToSurvey(session!.user!.email!, code, page);
	if (!accessResponse.ok) {
		error(accessResponse.status, { message: await accessResponse.json() });
	}

	const usersResponse = await getUsers();
	if (!usersResponse.ok) {
		error(usersResponse.status, { message: await usersResponse.json() });
	}

	const usersWithAccess: string[] = await accessResponse.json();
	const allUsers: string[] = await usersResponse.json();

	return { usersWithAccess, allUsers };
};
