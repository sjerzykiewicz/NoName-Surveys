import { fail, redirect } from '@sveltejs/kit';
import type { Actions } from './$types';

export const actions: Actions = {
	default: async ({ request, fetch }) => {
		const data = await request.formData();
		const code = data.get('survey-code');

		if (code === null || code === '') {
			return fail(422, {
				description: code,
				error: 'Please enter code.'
			});
		}

		if (!/^[0-9]{6}$/.test(code.toString())) {
			return fail(422, {
				description: code,
				error: 'Code must be 6 digits long.'
			});
		}

		const response = await fetch(`/api/surveys/fetch`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ survey_code: code })
		});
		if (!response.ok) {
			return fail(404, { error: 'Survey not found.' });
		}

		redirect(303, `/fill?code=${code}`);
	}
};
