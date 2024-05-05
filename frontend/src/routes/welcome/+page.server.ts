import { fail, redirect } from '@sveltejs/kit';
import type { Actions } from './$types';

export const actions = {
	default: async ({ request }) => {
		const data = await request.formData();
		const code = data.get('survey-code');
		if (code === null || code === '') {
			return fail(422, {
				description: code,
				error: 'Please enter code'
			});
		}
		if (!/^[0-9]{6}$/.test(code.toString())) {
			return fail(422, {
				description: code,
				error: 'Code must be 6 characters long and contain only digits'
			});
		}

		return redirect(303, `/fill/${code}`);
	}
} satisfies Actions;
