import type { PageServerLoad } from './$types';
import { getSurveyDrafts } from '$lib/server/database';
import { error, redirect } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ parent, params }) => {
	const { session } = await parent();
	if (!session) {
		redirect(303, `/account`);
	}

	const page = parseInt(params.page);

	const response = await getSurveyDrafts(session.user!.email!, page);
	if (!response.ok) {
		error(response.status, { message: await response.json() });
	}
	const drafts: {
		id: number;
		title: string;
		creation_date: string;
	}[] = await response.json();

	return { drafts };
};
