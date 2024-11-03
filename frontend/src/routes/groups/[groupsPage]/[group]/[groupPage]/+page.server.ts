import type { PageServerLoad } from './$types';
import { getUserGroup } from '$lib/server/database';
import { error } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ parent, params }) => {
	const { session } = await parent();
	if (!session) {
		error(401, 'You must be logged in to access this page.');
	}

	const group = params.group;
	const page = parseInt(params.groupPage);

	const response = await getUserGroup(session.user!.email!, group, page);
	if (!response.ok) {
		error(response.status, { message: await response.json() });
	}
	const users: { email: string; has_public_key: boolean }[] = await response.json();

	return { group, users };
};
