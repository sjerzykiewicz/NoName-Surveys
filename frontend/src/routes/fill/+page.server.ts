import type { PageServerLoad } from './$types';
import { getSurvey } from '$lib/server/database';
import { error } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ parent, url }) => {
	const session = await parent();
	const survey_code = url.searchParams.get('code');

	if (survey_code === null) {
		error(404);
	}

	const response = await getSurvey(survey_code);
	if (!response.ok) {
		error(response.status, { message: await response.json() });
	}
	const { survey_structure, uses_cryptographic_module, public_keys } = await response.json();

	return { session, survey_structure, uses_cryptographic_module, public_keys, survey_code };
};
