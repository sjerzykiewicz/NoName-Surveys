import { SvelteKitAuth } from '@auth/sveltekit';
import Google from '@auth/sveltekit/providers/google';
import { env } from '$env/dynamic/private';
import * as db from '$lib/server/database';

export const { handle } = SvelteKitAuth({
	providers: [
		Google({
			clientId: env.GOOGLE_CLIENT_ID,
			clientSecret: env.GOOGLE_CLIENT_SECRET
		})
	],
	trustHost: true,
	secret: env.AUTH_SECRET,
	session: {
		maxAge: 60 * 60 * 2,
		updateAge: 60 * 5
	},
	callbacks: {
		async jwt({ token, user }) {
			if (user) {
				const isUserRegistered = await db.validateUser(user.email!);
				if (!isUserRegistered) {
					await db.registerUser(user.email!);
				}
			}
			return token;
		}
	}
});
