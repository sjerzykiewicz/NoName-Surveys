import { fail, redirect } from '@sveltejs/kit';
import type { Actions } from './$types';
import * as db from '$lib/server/database';

export const actions: Actions = {
	default: async ({ request }) => {
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
				error: 'Code must be 6 characters long and contain only digits.'
			});
		}

		try {
			await db.getSurveyByCode(code.toString());
		} catch (e) {
			return fail(404, { description: code, error: 'Survey not found' });
		}

		redirect(303, `/${code}/fill`);
	}
};
