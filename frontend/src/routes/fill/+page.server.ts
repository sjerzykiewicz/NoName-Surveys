import type { Actions } from './$types';

export const actions: Actions = {
	default: async ({ request }) => {
		request.formData();
		// TODO signature, send to backend
	}
};
