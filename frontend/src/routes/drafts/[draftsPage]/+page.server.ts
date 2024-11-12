import type { PageServerLoad } from './$types';
import { countSurveyDrafts, getSurveyDrafts } from '$lib/server/database';
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

	const countResponse = await countSurveyDrafts(user_email);
	if (!countResponse.ok) {
		error(countResponse.status, { message: await countResponse.json() });
	}
	const numDrafts: number = await countResponse.json();

	return { drafts, numDrafts };
};
