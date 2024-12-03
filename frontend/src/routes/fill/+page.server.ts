import type { PageServerLoad } from './$types';
import { error } from '@sveltejs/kit';
import Survey from '$lib/entities/surveys/Survey';

export const load: PageServerLoad = async ({ url }) => {
	const survey_code = url.searchParams.get('code');
	const host = url.origin;

	if (survey_code === null) {
		error(404, { message: 'Survey not found' });
	}

	const response = await fetch(`${host}/api/surveys/fetch`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ survey_code })
	});
	if (!response.ok) {
		error(response.status, { message: await response.json() });
	}
	const survey: {
		title: string;
		survey_structure: Survey;
		survey_code: string;
		uses_cryptographic_module: boolean;
		public_keys: string[];
	} = await response.json();

	return { survey };
};
