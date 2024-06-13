import * as db from '$lib/server/database';
import { responseErrorHandler } from '$lib/utils/responseErrorHandler';
import type { PageServerLoad } from '../$types';
import { redirect } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ parent }) => {
	const { session } = await parent();
	if (!session) {
		redirect(303, `/account?redirectTo=/drafts`);
	}

	const response = await db.getDraftsOfUser(session.user!.email!);
	if (!response.ok) {
		responseErrorHandler(response);
	}
	const data = await response.json();
	return { drafts: data };
};
