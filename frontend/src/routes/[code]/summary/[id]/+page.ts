import type { PageLoad } from './$types';

export const load: PageLoad = async ({ params, parent }) => {
	const id = params.id;
	const { answers } = await parent();
	return { answers, id };
};
