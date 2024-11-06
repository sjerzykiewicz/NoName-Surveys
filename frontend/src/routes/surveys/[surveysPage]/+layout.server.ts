import type { LayoutServerLoad } from './$types';
import { getSurveys, countSurveys } from '$lib/server/database';
import { error, redirect } from '@sveltejs/kit';

export const load: LayoutServerLoad = async ({ parent, params }) => {
	const { session } = await parent();
	if (!session) {
		redirect(303, `/account`);
	}

	const page = parseInt(params.surveysPage);

	const surveysResponse = await getSurveys(session.user!.email!, page);
	if (!surveysResponse.ok) {
		error(surveysResponse.status, { message: await surveysResponse.json() });
	}
	const survey_list: {
		title: string;
		survey_code: string;
		creation_date: string;
		uses_cryptographic_module: boolean;
		is_owned_by_user: boolean;
		group_size: number;
	}[] = await surveysResponse.json();

	const countResponse = await countSurveys(session.user!.email!);
	if (!countResponse.ok) {
		error(countResponse.status, { message: await countResponse.json() });
	}
	const numSurveys: number = await countResponse.json();

	return { survey_list, numSurveys };
};
