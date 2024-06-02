import type { PageServerLoad } from './$types';
import * as db from '$lib/server/database';

export const load: PageServerLoad = async ({ params, parent }) => {
	const session = await parent();
	const survey_code = params.code;
	const { survey_structure, uses_cryptographic_module, public_keys } =
		await db.getSurveyByCode(survey_code);
	return { session, survey_structure, uses_cryptographic_module, public_keys };
};
