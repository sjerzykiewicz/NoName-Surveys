import type { LayoutServerLoad } from './$types';
import { getSurveys } from '$lib/server/database';
import { error, redirect } from '@sveltejs/kit';

export const load: LayoutServerLoad = async ({ parent, params }) => {
	const { session } = await parent();
	if (!session) {
		redirect(303, `/account`);
	}

	const page = parseInt(params.surveysPage);

	const response = await getSurveys(session.user!.email!, page);
	if (!response.ok) {
		error(response.status, { message: await response.json() });
	}
	const survey_list: {
		title: string;
		survey_code: string;
		creation_date: string;
		uses_cryptographic_module: boolean;
		is_owned_by_user: boolean;
		group_size: number;
	}[] = await response.json();

	return { survey_list };
};
