import type { PageServerLoad } from './$types';
import { error } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ parent, url }) => {
	const { session } = await parent();
	if (!session) {
		return { session, hasKey: false, keyCreationDate: '' };
	}

	const host = url.origin;

	const keyResponse = await fetch(`${host}/api/users/has-public-key`);
	if (!keyResponse.ok) {
		error(keyResponse.status, { message: await keyResponse.json() });
	}
	const hasKey: boolean = await keyResponse.json();

	const dateResponse = await fetch(`${host}/api/users/get-key-creation-date`);
	if (!dateResponse.ok) {
		error(dateResponse.status, { message: await dateResponse.json() });
	}
	const keyCreationDate: string = await dateResponse.json();

	return { session, hasKey, keyCreationDate };
};
