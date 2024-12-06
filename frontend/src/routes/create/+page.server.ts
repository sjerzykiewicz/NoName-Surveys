import type { PageServerLoad } from './$types';
import { error, redirect } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ parent, fetch }) => {
	const { session } = await parent();
	if (!session) {
		redirect(303, `/account`);
	}

	const groupsResponse = await fetch(`/api/groups/all-with-public-keys`);
	if (!groupsResponse.ok) {
		error(groupsResponse.status, { message: await groupsResponse.json() });
	}
	const group_list: string[] = await groupsResponse.json();

	const usersResponse = await fetch(`/api/users/all-with-public-keys`);
	if (!usersResponse.ok) {
		error(usersResponse.status, { message: await usersResponse.json() });
	}
	const user_list: string[] = await usersResponse.json();

	const draftCountResponse = await fetch(`/api/surveys/drafts/count`);
	if (!draftCountResponse.ok) {
		error(draftCountResponse.status, { message: await draftCountResponse.json() });
	}
	const numDrafts: number = await draftCountResponse.json();

	const surveyCountResponse = await fetch(`/api/surveys/count`);
	if (!surveyCountResponse.ok) {
		error(surveyCountResponse.status, { message: await surveyCountResponse.json() });
	}
	const numSurveys: number = await surveyCountResponse.json();

	return { group_list, user_list, numDrafts, numSurveys };
};
