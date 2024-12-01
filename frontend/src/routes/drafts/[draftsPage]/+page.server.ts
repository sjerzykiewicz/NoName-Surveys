import type { PageServerLoad } from './$types';
import {
	countSurveyDrafts,
	getSurveyDrafts,
	getUserGroupsWithKeys,
	getUsersWithKeys,
	countSurveys
} from '$lib/server/database';
import { error, redirect } from '@sveltejs/kit';
import { getEmail } from '$lib/utils/getEmail';

export const load: PageServerLoad = async ({ parent, params, cookies }) => {
	const { session } = await parent();
	if (!session) {
		redirect(303, `/account`);
	}

	const page = parseInt(params.draftsPage);

	const sessionCookie = cookies.get('user_session');
	const user_email = await getEmail(sessionCookie ?? '');

	const draftsResponse = await getSurveyDrafts(user_email, page);
	if (!draftsResponse.ok) {
		error(draftsResponse.status, { message: await draftsResponse.json() });
	}
	const drafts: {
		id: number;
		title: string;
		creation_date: string;
	}[] = await draftsResponse.json();

	const draftCountResponse = await countSurveyDrafts(user_email);
	if (!draftCountResponse.ok) {
		error(draftCountResponse.status, { message: await draftCountResponse.json() });
	}
	const numDrafts: number = await draftCountResponse.json();

	const surveyCountResponse = await countSurveys(user_email);
	if (!surveyCountResponse.ok) {
		error(surveyCountResponse.status, { message: await surveyCountResponse.json() });
	}
	const numSurveys: number = await surveyCountResponse.json();

	const groupsResponse = await getUserGroupsWithKeys(user_email);
	if (!groupsResponse.ok) {
		error(groupsResponse.status, { message: await groupsResponse.json() });
	}
	const group_list: string[] = await groupsResponse.json();

	const usersResponse = await getUsersWithKeys();
	if (!usersResponse.ok) {
		error(usersResponse.status, { message: await usersResponse.json() });
	}
	const user_list: string[] = await usersResponse.json();

	return { drafts, numDrafts, numSurveys, group_list, user_list };
};
