import type { RequestHandler } from '@sveltejs/kit';
import { getOAuthInstance } from '$lib/oauth1';
import { error } from '@sveltejs/kit';
import { env } from '$env/dynamic/private';

export const POST: RequestHandler = async () => {
	const oauth = getOAuthInstance();

	const requestData = {
		url: 'https://usosapps.amu.edu.pl/services/oauth/request_token?scopes=email',
		method: 'POST',
		data: {
			oauth_callback: env.ORIGIN + '/api/oauth/callback'
		}
	};

	try {
		const oauthData = oauth.authorize(requestData);

		const response = await fetch(requestData.url, {
			method: 'POST',
			headers: oauth.toHeader(oauthData)
		});

		if (!response.ok) {
			throw error(response.status, 'Failed to obtain request token');
		}

		const responseText = await response.text();
		const params = new URLSearchParams(responseText);
		const responseData = Object.fromEntries(params.entries());

		return new Response(JSON.stringify(responseData), {
			status: 200,
			headers: {
				'Content-Type': 'application/json'
			}
		});
	} catch (err) {
		console.error('Error fetching request token:', err);
		throw error(500, 'Failed to obtain request token');
	}
};
