import type { RequestHandler } from './$types';
import * as db from '$lib/server/database';
import { json } from '@sveltejs/kit';

export const GET: RequestHandler = async () => {
	const response = await db.getAllUsers();
	return json({ response });
};
