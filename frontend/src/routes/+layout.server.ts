import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async ({ locals }) => {
	return {
		session: locals.user
			? {
					user: {
						email: locals.user?.email as string
					}
				}
			: null
	};
};
