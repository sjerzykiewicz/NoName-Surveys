import type { PageServerLoad } from './$types';
import { checkAccessToSurvey, getUsers, countUsersWithAccess } from '$lib/server/database';
import { error } from '@sveltejs/kit';
import { getEmail } from '$lib/utils/getEmail';

export const load: PageServerLoad = async ({ params, cookies }) => {
	const code = params.code;
	const page = parseInt(params.accessPage);

	const sessionCookie = cookies.get('user_session');
	const user_email = await getEmail(sessionCookie ?? '');

	const accessResponse = await checkAccessToSurvey(user_email, code, page);
	if (!accessResponse.ok) {
		error(accessResponse.status, { message: await accessResponse.json() });
	}
	const usersWithAccess: string[] = await accessResponse.json();

	const usersResponse = await getUsers();
	if (!usersResponse.ok) {
		error(usersResponse.status, { message: await usersResponse.json() });
	}
	const allUsers: string[] = await usersResponse.json();

	const countResponse = await countUsersWithAccess(user_email, code);
	if (!countResponse.ok) {
		error(countResponse.status, { message: await countResponse.json() });
	}
	const numUsers = await countResponse.json();

	return { usersWithAccess, allUsers, numUsers };
};
