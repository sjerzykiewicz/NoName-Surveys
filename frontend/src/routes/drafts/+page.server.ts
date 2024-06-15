import * as db from '$lib/server/database';
import type { PageServerLoad } from '../$types';
import { error, redirect } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ parent }) => {
	const { session } = await parent();
	if (!session) {
		redirect(303, `/account`);
	}

	const response = await db.getDraftsOfUser(session.user!.email!);
	if (!response.ok) {
		error(response.status, { message: await response.json() });
	}
	const data = await response.json();
	return { drafts: data };
};
