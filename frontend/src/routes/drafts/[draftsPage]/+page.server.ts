import type { PageServerLoad } from './$types';
import { error, redirect } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ parent, params, fetch }) => {
	const { session } = await parent();
	if (!session) {
		redirect(303, `/account`);
	}

	const page = parseInt(params.draftsPage);

	const draftsResponse = await fetch(`/api/surveys/drafts/all`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ page })
	});
	if (!draftsResponse.ok) {
		error(draftsResponse.status, { message: await draftsResponse.json() });
	}
	const drafts: {
		id: number;
		title: string;
		creation_date: string;
	}[] = await draftsResponse.json();

	let retries = 2;
	while (retries > 0) {
		try {
			const [draftCountResponse, surveyCountResponse, groupsResponse, usersResponse] =
				await Promise.all([
					fetch(`/api/surveys/drafts/count`),
					fetch(`/api/surveys/count`),
					fetch(`/api/groups/all-with-public-keys`),
					fetch(`/api/users/all-with-public-keys`)
				]);

			if (!draftCountResponse.ok) {
				throw error(draftCountResponse.status, { message: await draftCountResponse.json() });
			}
			const numDrafts: number = await draftCountResponse.json();

			if (!surveyCountResponse.ok) {
				throw error(surveyCountResponse.status, { message: await surveyCountResponse.json() });
			}
			const numSurveys: number = await surveyCountResponse.json();

			if (!groupsResponse.ok) {
				throw error(groupsResponse.status, { message: await groupsResponse.json() });
			}
			const group_list: string[] = await groupsResponse.json();

			if (!usersResponse.ok) {
				throw error(usersResponse.status, { message: await usersResponse.json() });
			}
			const user_list: string[] = await usersResponse.json();

			return {
				drafts,
				numDrafts,
				numSurveys,
				group_list,
				user_list
			};
		} catch (err) {
			console.error(err);
			retries--;
			if (retries === 0) {
				throw error(500, { message: 'Failed to fetch data after multiple attempts' });
			}
		}
	}
};
