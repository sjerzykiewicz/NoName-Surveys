import { _getUserInfo } from '../../routes/api/oauth/user/+server';
import { error } from '@sveltejs/kit';

export async function getEmail(sessionCookie: string): Promise<string> {
	if (sessionCookie) {
		const sessionCookieJson = JSON.parse(sessionCookie);
		let retries = 2;
		while (retries > 0) {
			try {
				const userData = await _getUserInfo(
					sessionCookieJson.oauth_token,
					sessionCookieJson.oauth_token_secret
				);
				if (userData.email) {
					return userData.email;
				}
			} catch (err) {
				console.error(err);
				retries--;
			}
		}
		error(500, { message: 'Failed to get data from the USOS API. Please try reloading the page' });
	}
	error(401, { message: 'Unauthorized' });
}
