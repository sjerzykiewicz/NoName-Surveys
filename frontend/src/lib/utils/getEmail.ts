import { _getUserInfo } from '../../routes/api/oauth/user/+server';

export async function getEmail(sessionCookie: string) {
	if (sessionCookie) {
		const sessionCookieJson = JSON.parse(sessionCookie);
		const userData = await _getUserInfo(
			sessionCookieJson.oauth_token,
			sessionCookieJson.oauth_token_secret
		);
		return userData.email;
	}

	return '';
}
