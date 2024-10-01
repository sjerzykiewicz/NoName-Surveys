import type { PageServerLoad } from './$types';
import * as db from '$lib/server/database';
import { error } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ params, parent }) => {
	const { session } = await parent();
	if (!session) {
		error(401, 'You must be logged in to access this page.');
	}

	const response = await db.checkAccessToSurvey(session.user!.email!, params.code);
	if (!response.ok) {
		error(response.status, { message: await response.json() });
	}

	const users = await response.json();
	return { users };
};
