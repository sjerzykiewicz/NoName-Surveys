import { getOAuthInstance } from '$lib/server/oauth1';
import { env } from '$env/dynamic/private';
import { error } from '@sveltejs/kit';

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

	const responseUser = await fetch(requestDataUser.url, {
		method: 'GET',
		headers: oauth.toHeader(oauthDataUser)
	});

	if (!responseUser.ok) {
		return error(responseUser.status, { message: await responseUser.json() });
	}

	return responseUser.json();
}
