import type { PageServerLoad } from './$types';
import { error, redirect } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ parent, params, fetch }) => {
	const { session } = await parent();
	if (!session) {
		redirect(303, `/account`);
	}

	const page = parseInt(params.draftsPage);

	const draftsResponse = await fetch(`/api/surveys/drafts/all`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ page })
	});
	if (!draftsResponse.ok) {
		error(draftsResponse.status, { message: await draftsResponse.json() });
	}
	const drafts: {
		id: number;
		title: string;
		creation_date: string;
	}[] = await draftsResponse.json();

	const response = await fetch(`/api/combined/groups_users_drafts_surveys`);
	if (!response.ok) {
		throw error(response.status, { message: await response.json() });
	}
	const { groups, users, drafts_count, surveys_count } = await response.json();

	return {
		drafts,
		numDrafts: drafts_count,
		numSurveys: surveys_count,
		group_list: groups,
		user_list: users
	};
};
