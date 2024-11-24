import type SurveySummary from '$lib/entities/surveys/SurveySummary';
import type { PageServerLoad } from './$types';
import { error } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ cookies }) => {
	const summaryCookie = cookies.get('imported_summary');
	if (!summaryCookie) {
		error(404, { message: 'Summary not found' });
	}

	let importedSummary: SurveySummary[] = [];
	try {
		importedSummary = JSON.parse(decodeURIComponent(summaryCookie));
	} catch (e) {
		error(400, { message: 'Incorrect file format' });
	}
	return { importedSummary };
};
