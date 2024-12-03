import type { PageServerLoad } from './$types';
import { error, redirect } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ parent, params, url }) => {
	const { session } = await parent();
	if (!session) {
		redirect(303, `/account`);
	}

	const page = parseInt(params.draftsPage);
	const host = url.origin;

	const draftsResponse = await fetch(`${host}/api/surveys/drafts/all`, {
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

	const draftCountResponse = await fetch(`${host}/api/surveys/drafts/count`);
	if (!draftCountResponse.ok) {
		error(draftCountResponse.status, { message: await draftCountResponse.json() });
	}
	const numDrafts: number = await draftCountResponse.json();

	const surveyCountResponse = await fetch(`${host}/api/surveys/count`);
	if (!surveyCountResponse.ok) {
		error(surveyCountResponse.status, { message: await surveyCountResponse.json() });
	}
	const numSurveys: number = await surveyCountResponse.json();

	const groupsResponse = await fetch(`${host}/api/groups/all-with-public-keys`);
	if (!groupsResponse.ok) {
		error(groupsResponse.status, { message: await groupsResponse.json() });
	}
	const group_list: string[] = await groupsResponse.json();

	const usersResponse = await fetch(`${host}/api/users/all-with-public-keys`);
	if (!usersResponse.ok) {
		error(usersResponse.status, { message: await usersResponse.json() });
	}
	const user_list: string[] = await usersResponse.json();

	return { drafts, numDrafts, numSurveys, group_list, user_list };
};
