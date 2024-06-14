import type { PageServerLoad } from './$types';
import * as db from '$lib/server/database';
import { error, redirect } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ parent }) => {
	const { session } = await parent();
	if (!session) {
		redirect(303, `/account`);
	}

	const response = await db.getAllUsers();
	if (!response.ok) {
		error(response.status, { message: await response.json() });
	}

	const user_list = await response.json();
	return { session, user_list };
};
