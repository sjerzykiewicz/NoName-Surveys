import type { PageServerLoad } from './$types';
import { error, redirect } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ parent, params, fetch }) => {
	const { session } = await parent();
	if (!session) {
		redirect(303, `/account`);
	}

	const page = parseInt(params.draftsPage);

	const response = await fetch(`/api/combined/drafts`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ page })
	});

	if (!response.ok) {
		throw error(response.status, { message: await response.json() });
	}
	const { drafts, groups, users, drafts_count, surveys_count } = await response.json();

	return {
		drafts: drafts,
		numDrafts: drafts_count,
		numSurveys: surveys_count,
		group_list: groups,
		user_list: users
	};
};
