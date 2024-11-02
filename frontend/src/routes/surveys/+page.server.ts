import type { PageServerLoad } from '../$types';
import { getSurveys } from '$lib/server/database';
import { error, redirect } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ parent }) => {
	const { session } = await parent();
	if (!session) {
		redirect(303, `/account`);
	}

	const response = await getSurveys(session.user!.email!);
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
