## OAuth 2.0 demo authentication

```ts
// src/auth.ts
import { SvelteKitAuth } from '@auth/sveltekit';
import Google from '@auth/sveltekit/providers/google';
import GitHub from '@auth/sveltekit/providers/github';
import { env } from '$env/dynamic/private';
import * as db from '$lib/server/database';

export const { handle } = SvelteKitAuth({
	providers: [Google, GitHub],
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
```

```ts
// src/hooks.server.ts
export { handle } from './auth';
```

```ts
// src/lib/components/account-page/SignIn.svelte
import { signIn } from '@auth/sveltekit/client';

<h1>Sign in with:</h1>
<div class="sign-buttons">
	<button title="Google" class="sign-in" on:click={() => signIn('google')}
		><i class="fa-brands fa-google"></i></button
	>
	<button title="GitHub" class="sign-in" on:click={() => signIn('github')}
		><i class="fa-brands fa-github"></i></button
	>
	<button title="X" class="sign-in" disabled><i class="fa-brands fa-x-twitter"></i></button>
</div>
```

```ts
// src/lib/components/account-page/SignOut.svelte
import { signOut } from '@auth/sveltekit/client';
	<button title="Sign out" class="sign-out" on:click={() => signOut()}
		><i class="material-symbols-rounded">logout</i>Sign Out</button
	>
```
