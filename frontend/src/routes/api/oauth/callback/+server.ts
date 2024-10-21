import { type RequestHandler, error, redirect } from '@sveltejs/kit';
import { getOAuthInstance } from '$lib/oauth1';
import { env } from '$env/dynamic/private';
import * as db from '$lib/server/database';

export const GET: RequestHandler = async ({ url, cookies, locals }) => {
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
			throw new Error('Failed to fetch access token');
		}

		const responseText = await response.text();
		const params = new URLSearchParams(responseText);
		const responseData = Object.fromEntries(params.entries());

		const requestDataUser = {
			url: env.AUTH_USOS_BASE_URL + 'services/users/user?fields=email',
			method: 'GET'
		};

		const oauthDataUser = oauth.authorize(requestDataUser, {
			key: responseData.oauth_token,
			secret: responseData.oauth_token_secret
		});

		const responseUser = await fetch(requestDataUser.url, {
			method: 'GET',
			headers: oauth.toHeader(oauthDataUser)
		});

		if (!responseUser.ok) {
			throw error(responseUser.status, 'Failed to fetch user');
		}

		const userData = await responseUser.json();

		if (userData.email) {
			const isUserRegistered = await (await db.validateUser(userData.email!)).json();
			if (!isUserRegistered) {
				await db.registerUser(userData.email!);
			}
		}

		locals.user = {
			email: userData.email,
			oauth_token: responseData.oauth_token,
			oauth_token_secret: responseData.oauth_token_secret
		};

		cookies.set('user_session', JSON.stringify(locals.user), {
			path: '/',
			httpOnly: true,
			secure: true,
			maxAge: 60 * 60 * 2 // 2 hours
		});

		throw redirect(303, env.ORIGIN + '/account');
	} catch (err) {
		if (err instanceof Error) {
			console.error('Error fetching access token / user info:', err);
			throw error(500, 'Failed to obtain access token / user info');
		}
		throw err;
	}
};
