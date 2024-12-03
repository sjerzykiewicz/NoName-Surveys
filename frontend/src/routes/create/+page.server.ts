import type { PageServerLoad } from './$types';
import { error, redirect } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ parent, url }) => {
	const { session } = await parent();
	if (!session) {
		redirect(303, `/account`);
	}

	const host = url.origin;

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

	return { group_list, user_list, numDrafts, numSurveys };
};
