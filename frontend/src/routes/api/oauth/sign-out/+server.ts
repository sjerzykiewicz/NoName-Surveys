import type { RequestHandler } from '@sveltejs/kit';
import { getOAuthInstance } from '$lib/oauth1';
import { error, redirect } from '@sveltejs/kit';

export const POST: RequestHandler = async ({ cookies }) => {
	const session = cookies.get('user_session');
	const { oauth_token, oauth_token_secret } = JSON.parse(session || '{}');
	if (!oauth_token || !oauth_token_secret) {
		throw error(400, 'Missing oauth_token or oauth_token_secret');
	}

	const oauth = getOAuthInstance();

	const requestData = {
		url: 'https://usosapps.amu.edu.pl/services/oauth/revoke_token?oauth_token=' + oauth_token,
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

		if (!response.ok) {
			throw error(response.status, 'Failed to revoke access token');
		}

		cookies.delete('user_session', { path: '/' });

		throw redirect(302, '/account');
	} catch (err) {
		if (err instanceof Error) {
			console.error('Error revoking access token:', err);
			throw error(500, 'Error revoking access token:');
		}
		throw err;
	}
};
