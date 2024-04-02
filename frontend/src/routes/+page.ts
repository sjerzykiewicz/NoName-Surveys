import type { PageLoad } from './$types';

export const load: PageLoad = async ({ fetch }) => {
	return await fetch(`http://localhost:8000`, { method: 'GET' }).then((res) => res.json());
};
