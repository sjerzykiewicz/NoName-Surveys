import type { PageServerLoad } from './$types';
import {
	checkAccessToSurvey,
	getAllUsersWithoutAccess,
	countUsersWithAccess
} from '$lib/server/database';
import { error } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ parent, params }) => {
	const { session } = await parent();

	const code = params.code;
	const page = parseInt(params.accessPage);

	const accessResponse = await checkAccessToSurvey(session!.user!.email!, code, page);
	if (!accessResponse.ok) {
		error(accessResponse.status, { message: await accessResponse.json() });
	}
	const usersWithAccess: string[] = await accessResponse.json();

	const notAccessResponse = await getAllUsersWithoutAccess(session!.user!.email!, code);
	if (!notAccessResponse.ok) {
		error(notAccessResponse.status, { message: await notAccessResponse.json() });
	}
	const usersWithoutAccess: string[] = await notAccessResponse.json();

	const countResponse = await countUsersWithAccess(session!.user!.email!, code);
	if (!countResponse.ok) {
		error(countResponse.status, { message: await countResponse.json() });
	}
	const numUsers: number = await countResponse.json();

	return { usersWithAccess, usersWithoutAccess, numUsers };
};
