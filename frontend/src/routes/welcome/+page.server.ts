import { fail } from '@sveltejs/kit';
import type { Actions } from './$types';

export const actions = {
	default: async ({ request }) => {
		const data = await request.formData();
		const info = data.get('survey-code');
		if (info === null || info === '') {
			return fail(422, {
				description: info,
				error: 'Please enter code'
			});
		}
		if (!/^[0-9]{6}$/.test(info.toString())) {
			return fail(422, {
				description: info,
				error: 'Code must be 6 characters long and contain only digits'
			});
		}
	}
} satisfies Actions;
