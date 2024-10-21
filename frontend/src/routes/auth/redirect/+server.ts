import { redirect } from '@sveltejs/kit';
import type { RequestEvent } from '@sveltejs/kit';
import { env } from '$env/dynamic/private';

export const GET = async ({ url }: RequestEvent) => {
	const oauth_token = url.searchParams.get('oauth_token');

	if (!oauth_token) {
		return {
			status: 400,
			body: { error: 'Missing oauth_token' }
		};
	}

	const authorizationUrl =
		env.AUTH_USOS_BASE_URL + `services/oauth/authorize?oauth_token=${oauth_token}`;
	throw redirect(302, authorizationUrl);
};
