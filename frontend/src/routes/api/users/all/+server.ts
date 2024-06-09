import type { RequestHandler } from './$types';
import * as db from '$lib/server/database';

export const GET: RequestHandler = async () => {
	return db.getAllUsers();
};
