import type { LayoutServerLoad } from './$types';
import { getSurveys, countSurveys } from '$lib/server/database';
import { error, redirect } from '@sveltejs/kit';
import { getEmail } from '$lib/utils/getEmail';

export const load: LayoutServerLoad = async ({ parent, params, cookies }) => {
	const { session } = await parent();
	if (!session) {
		redirect(303, `/account`);
	}

	const page = parseInt(params.surveysPage);

	const sessionCookie = cookies.get('user_session');
	const user_email = await getEmail(sessionCookie ?? '');

	const surveysResponse = await getSurveys(user_email, page);
	if (!surveysResponse.ok) {
		error(surveysResponse.status, { message: await surveysResponse.json() });
	}
	const surveys: {
		title: string;
		survey_code: string;
		creation_date: string;
		uses_cryptographic_module: boolean;
		is_owned_by_user: boolean;
		group_size: number;
	}[] = await surveysResponse.json();

	const countResponse = await countSurveys(user_email);
	if (!countResponse.ok) {
		error(countResponse.status, { message: await countResponse.json() });
	}
	const numSurveys: number = await countResponse.json();

	return { surveys, numSurveys };
};
