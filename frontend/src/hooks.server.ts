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

		if (userData && Object.keys(userData).length === 0) {
			event.cookies.delete('user_session', { path: '/' });
			event.cookies.delete('oauth_token_secret', { path: '/' });
		} else {
			event.locals.user = {
				email: userData.email as string
			};
		}
	}

	const response = await resolve(event);

	return response;
};
