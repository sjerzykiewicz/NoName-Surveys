// import { SvelteKitAuth } from '@auth/sveltekit';
// import Google from '@auth/sveltekit/providers/google';
// import GitHub from '@auth/sveltekit/providers/github';
// import { env } from '$env/dynamic/private';
// import * as db from '$lib/server/database';

// export const { handle } = SvelteKitAuth({
// 	providers: [
// 		Google,
// 		GitHub
// 	],
// 	trustHost: true,
// 	debug: true,
// 	secret: env.AUTH_SECRET,
// 	session: {
// 		maxAge: 60 * 60 * 2,
// 		updateAge: 60 * 5
// 	},
// 	callbacks: {
// 		async jwt({ token, user }) {
// 			if (user) {
// 				const isUserRegistered = await (await db.validateUser(user.email!)).json();
// 				if (!isUserRegistered) {
// 					await db.registerUser(user.email!);
// 				}
// 			}
// 			return token;
// 		}
// 	}
// });
