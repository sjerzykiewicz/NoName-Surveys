import type { RequestHandler } from './$types';
import { getUsersWithKeys } from '$lib/server/database';

export const GET: RequestHandler = async () => {
	return getUsersWithKeys();
};
