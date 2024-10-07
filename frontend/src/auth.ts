import { SvelteKitAuth } from '@auth/sveltekit';
import Google from '@auth/sveltekit/providers/google';
import GitHub from '@auth/sveltekit/providers/github';
import { env } from '$env/dynamic/private';
import * as db from '$lib/server/database';

export const { handle } = SvelteKitAuth({
	providers: [
		Google,
		GitHub,
		{
			id: 'usos', // signIn("my-provider") and will be part of the callback URL
			name: 'Usos', // optional, used on the default login page as the button text.
			type: 'oidc', // or "oauth" for OAuth 2 providers
			issuer: 'https://usosapps.amu.edu.pl', // to infer the .well-known/openid-configuration URL
			authorization: {
				url: 'https://usosapps.amu.edu.pl/services/oauth2/impersonated_token'
			},
			clientId: env.AUTH_USOS_ID, // from the provider's dashboard
			clientSecret: env.AUTH_USOS_SECRET // from the provider's dashboard
		}
	],
	trustHost: true,
	debug: true,
	secret: env.AUTH_SECRET,
	session: {
		maxAge: 60 * 60 * 2,
		updateAge: 60 * 5
	},
	callbacks: {
		async jwt({ token, user }) {
			if (user) {
				const isUserRegistered = await (await db.validateUser(user.email!)).json();
				if (!isUserRegistered) {
					await db.registerUser(user.email!);
				}
			}
			return token;
		}
	}
});
