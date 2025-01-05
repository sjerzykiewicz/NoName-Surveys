import type { PageServerLoad } from './$types';
import { error, redirect } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ parent, fetch }) => {
	const { session } = await parent();
	if (!session) {
		redirect(303, `/account`);
	}

	const response = await fetch(`/api/combined/create`);
	if (!response.ok) {
		throw error(response.status, { message: await response.json() });
	}
	const { groups, users, drafts_count, surveys_count } = await response.json();

	return {
		group_list: groups,
		user_list: users,
		numDrafts: drafts_count,
		numSurveys: surveys_count
	};
};
