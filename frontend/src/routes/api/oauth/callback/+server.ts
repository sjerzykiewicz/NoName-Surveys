import { type RequestHandler, error, redirect } from '@sveltejs/kit';
import { getOAuthInstance } from '$lib/oauth1';
import { env } from '$env/dynamic/private';
import { validateUser, createUser } from '$lib/server/database';
import { _getUserInfo } from '../user/+server';

export const GET: RequestHandler = async ({ url, cookies, locals }) => {
	const err = url.searchParams.get('error');
	if (err) {
		throw redirect(303, env.ORIGIN + '/account');
	}
	const oauth_token = url.searchParams.get('oauth_token');
	const oauth_verifier = url.searchParams.get('oauth_verifier');
	const oauth_token_secret = cookies.get('oauth_token_secret');

	if (!oauth_token || !oauth_verifier || !oauth_token_secret) {
		console.error('Missing oauth_token or oauth_verifier or oauth_token_secret');
		throw error(400, 'Missing oauth_token or oauth_verifier or oauth_token_secret');
	}

	const oauth = getOAuthInstance();

	const requestData = {
		url: env.AUTH_USOS_BASE_URL + 'services/oauth/access_token',
		method: 'POST',
		data: { oauth_verifier }
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
			throw error(response.status, `Failed to fetch access token: ${response.statusText}`);
		}

		const responseText = await response.text();
		const params = new URLSearchParams(responseText);
		const responseData = Object.fromEntries(params.entries());

		const userData = await _getUserInfo(responseData.oauth_token, responseData.oauth_token_secret);

		if (userData.email) {
			const isUserRegistered = await (await validateUser(userData.email)).json();
			if (!isUserRegistered) {
				await createUser(userData.email);
			}
		}

		locals.user = {
			email: userData.email
		};

		const tokens = {
			oauth_token: responseData.oauth_token,
			oauth_token_secret: responseData.oauth_token_secret
		};

		cookies.set('user_session', JSON.stringify(tokens), {
			path: '/',
			httpOnly: true,
			secure: true,
			maxAge: 60 * 60 * 2 // 2 hours
		});

		const from = cookies.get('from');
		if (from) {
			throw redirect(303, from);
		}

		throw redirect(303, env.ORIGIN + '/account');
	} catch (err) {
		if (err instanceof Error) {
			console.error('Error fetching access token / user info:', err);
			throw error(500, 'Failed to obtain access token / user info');
		}
		throw err;
	}
};
