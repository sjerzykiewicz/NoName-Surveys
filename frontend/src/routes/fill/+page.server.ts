import type { PageServerLoad } from './$types';
import { getSurvey } from '$lib/server/database';
import { error } from '@sveltejs/kit';
import Survey from '$lib/entities/surveys/Survey';

export const load: PageServerLoad = async ({ url }) => {
	const survey_code = url.searchParams.get('code');

	if (survey_code === null) {
		error(404);
	}

	const response = await getSurvey(survey_code);
	if (!response.ok) {
		error(response.status, { message: await response.json() });
	}
	const survey: {
		survey_structure: Survey;
		survey_code: string;
		uses_cryptographic_module: boolean;
		public_keys: string[];
	} = await response.json();

	return { survey };
};
