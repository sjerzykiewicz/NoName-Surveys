import { redirect } from '@sveltejs/kit';
import type { RequestEvent } from '@sveltejs/kit';

export const GET = async ({ url, cookies }: RequestEvent) => {
	const oauth_token = url.searchParams.get('oauth_token');
	const oauth_token_secret = url.searchParams.get('oauth_token_secret');

	if (oauth_token_secret) {
		cookies.set('oauth_token_secret', oauth_token_secret, {
			path: '/',
			httpOnly: true,
			secure: true,
			sameSite: 'strict',
			maxAge: 60 * 5 // 5 minutes
		});
	}

	if (!oauth_token) {
		return {
			status: 400,
			body: { error: 'Missing oauth_token' }
		};
	}

	const authorizationUrl = `https://usosapps.amu.edu.pl/services/oauth/authorize?oauth_token=${oauth_token}`;
	throw redirect(302, authorizationUrl);
};
