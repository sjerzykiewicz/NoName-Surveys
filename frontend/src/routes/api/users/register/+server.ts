// import type { RequestHandler } from '../../surveys/create/$types';
// import * as db from '$lib/server/database';
// import { json } from '@sveltejs/kit';

// export const POST: RequestHandler = async ({ request }) => {
// 	const { email } = await request.json();
// 	const isUserRegistered = await db.validateUser(email);
// 	if (!isUserRegistered) {
// 		await db.registerUser(email); // TODO - for now pass email as key to ensure uniqueness
// 	}
// 	return json({ status: 200 });
// };
