import type { PageServerLoad } from './$types';
import { countSurveyDrafts, getSurveyDrafts } from '$lib/server/database';
import { error, redirect } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ parent, params }) => {
	const { session } = await parent();
	if (!session) {
		redirect(303, `/account`);
	}

	const page = parseInt(params.draftsPage);

	const draftsResponse = await getSurveyDrafts(session.user!.email!, page);
	if (!draftsResponse.ok) {
		error(draftsResponse.status, { message: await draftsResponse.json() });
	}
	const drafts: {
		id: number;
		title: string;
		creation_date: string;
	}[] = await draftsResponse.json();

	const countResponse = await countSurveyDrafts(session.user!.email!);
	if (!countResponse.ok) {
		error(countResponse.status, { message: await countResponse.json() });
	}
	const numDrafts: number = await countResponse.json();

	return { drafts, numDrafts };
};
