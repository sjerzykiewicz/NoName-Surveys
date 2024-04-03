import type { PageLoad } from './$types';

export const load: PageLoad = async ({ fetch }) => {
	try {
		const response = await fetch(`http://localhost:8000`, { method: 'GET' });
		if (!response.ok) {
			throw new Error('Failed to fetch data from the API');
		}
		return await response.json();
	} catch (error) {
		console.error('An error occurred while fetching data:', error);
		return null;
	}
};
