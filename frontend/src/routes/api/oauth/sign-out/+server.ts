import type { RequestHandler } from '@sveltejs/kit';
import { getOAuthInstance } from '$lib/server/oauth1';
import { error, redirect } from '@sveltejs/kit';
import { env } from '$env/dynamic/private';

export const POST: RequestHandler = async ({ cookies }) => {
	const session = cookies.get('user_session');
	const { oauth_token, oauth_token_secret } = JSON.parse(session || '{}');
	if (!oauth_token || !oauth_token_secret) {
		throw error(400, 'Missing oauth_token or oauth_token_secret');
	}

	const oauth = getOAuthInstance();

	const requestData = {
		url: env.AUTH_USOS_BASE_URL + 'services/oauth/revoke_token?oauth_token=' + oauth_token,
		method: 'POST'
	};

	try {
		const oauthData = oauth.authorize(requestData, {
			key: oauth_token,
			secret: oauth_token_secret
		});

		const response = await fetch(requestData.url, {
			method: 'POST',
			headers: oauth.toHeader(oauthData)
		});

		cookies.delete('user_session', { path: '/' });
		cookies.delete('oauth_token_secret', { path: '/' });

		if (!response.ok) {
			throw error(response.status, 'Failed to revoke access token');
		}

		throw redirect(302, '/account');
	} catch (err) {
		if (err instanceof Error) {
			console.error('Error revoking access token:', err);
			throw error(500, 'Error revoking access token:');
		}
		throw err;
	}
};
