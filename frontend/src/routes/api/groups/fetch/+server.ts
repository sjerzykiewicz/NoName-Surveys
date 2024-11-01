import type { RequestHandler } from './$types';
import * as db from '$lib/server/database';
import { _getUserInfo } from '../../oauth/user/+server';

export const POST: RequestHandler = async ({ request, cookies }) => {
	const sessionCookie = cookies.get('user_session');
	let user_email = '';
	if (sessionCookie) {
		const sessionCookieJson = JSON.parse(sessionCookie);
		const userData = await _getUserInfo(
			sessionCookieJson.oauth_token,
			sessionCookieJson.oauth_token_secret
		);
		user_email = userData.email;
	}
	const { name } = await request.json();
	return db.getUserGroup(user_email, name);
};
