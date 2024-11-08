import type { Handle } from '@sveltejs/kit';
import { _getUserInfo } from './routes/api/oauth/user/+server';

export const handle: Handle = async ({ event, resolve }) => {
	const sessionCookie = event.cookies.get('user_session');

	if (sessionCookie) {
		const sessionCookieJson = JSON.parse(sessionCookie);
		const userData = await _getUserInfo(
			sessionCookieJson.oauth_token,
			sessionCookieJson.oauth_token_secret
		);

		event.locals.user = {
			email: userData.email
		};
	}

	const response = await resolve(event);

	return response;
};
