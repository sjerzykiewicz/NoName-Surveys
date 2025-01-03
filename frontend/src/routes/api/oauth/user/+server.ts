import { getOAuthInstance } from '$lib/oauth1';
import { env } from '$env/dynamic/private';

export async function _getUserInfo(oauth_token: string, oauth_token_secret: string) {
	const oauth = getOAuthInstance();

	const requestDataUser = {
		url: env.AUTH_USOS_BASE_URL + 'services/users/user?fields=email',
		method: 'GET'
	};

	const oauthDataUser = oauth.authorize(requestDataUser, {
		key: oauth_token,
		secret: oauth_token_secret
	});

	const fetchWithTimeout = async (url: string, options: RequestInit, timeout: number) => {
		const controller = new AbortController();
		const timeoutId = setTimeout(() => controller.abort(), timeout);
		const response = await fetch(url, { ...options, signal: controller.signal });
		clearTimeout(timeoutId);
		return response;
	};

	try {
		const responseUser = await fetchWithTimeout(
			requestDataUser.url,
			{
				method: 'GET',
				headers: oauth.toHeader(oauthDataUser)
			},
			11000
		); // 11000 ms timeout because USOS API timeout is 10s

		if (!responseUser.ok) {
			console.log('Error fetching user info', responseUser);
			return {};
		}

		return responseUser.json();
	} catch (err) {
		console.error('Fetch failed:', err);
		return {};
	}
}
