import { SvelteKitAuth } from '@auth/sveltekit';
import Google from '@auth/sveltekit/providers/google';
import { env } from '$env/dynamic/private';

export const { handle } = SvelteKitAuth({
	providers: [
		Google({
			clientId: env.GOOGLE_CLIENT_ID,
			clientSecret: env.GOOGLE_CLIENT_SECRET
		})
	],
	trustHost: true,
	session: {
		maxAge: 60 * 60 * 2,
		updateAge: 60 * 5
	}
});
