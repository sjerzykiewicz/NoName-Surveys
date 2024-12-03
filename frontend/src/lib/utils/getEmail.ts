import { _getUserInfo } from '../../routes/api/oauth/user/+server';
import { error } from '@sveltejs/kit';

export async function getEmail(sessionCookie: string): Promise<string> {
	if (sessionCookie) {
		const sessionCookieJson = JSON.parse(sessionCookie);
		const userData = await _getUserInfo(
			sessionCookieJson.oauth_token,
			sessionCookieJson.oauth_token_secret
		);
		if (userData.email) {
			return userData.email;
		}
	}
	error(401, 'Unauthorized');
}
