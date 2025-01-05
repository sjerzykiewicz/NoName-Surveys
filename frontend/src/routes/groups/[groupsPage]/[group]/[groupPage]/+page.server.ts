import type { PageServerLoad } from './$types';
import { error } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ parent, params, fetch }) => {
	const { session } = await parent();
	if (!session) {
		error(401, 'You must be logged in to access this page.');
	}

	const group = params.group;
	const page = parseInt(params.groupPage);

	const response = await fetch('/api/combined/members', {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify({ group, page })
	});
	if (!response.ok) {
		throw error(response.status, { message: await response.json() });
	}

	const { members, notMembers, count } = await response.json();

	return {
		group,
		members,
		notMembers,
		numNembers: count
	};
};
