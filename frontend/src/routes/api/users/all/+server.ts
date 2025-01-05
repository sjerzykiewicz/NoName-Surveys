import type { RequestHandler } from './$types';
import { getUsers } from '$lib/server/database';

export const GET: RequestHandler = async () => {
	return getUsers();
};
