import type { LayoutServerLoad } from './$types';
import { error, redirect } from '@sveltejs/kit';

export const load: LayoutServerLoad = async ({ parent, params, fetch }) => {
	const { session } = await parent();
	if (!session) {
		redirect(303, `/account`);
	}

	const page = parseInt(params.surveysPage);

	const response = await fetch('/api/combined/surveys', {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify({ page })
	});

	if (!response.ok) {
		throw error(response.status, { message: await response.json() });
	}

	const { surveys, count } = await response.json();

	return {
		surveys,
		numSurveys: count
	};
};
