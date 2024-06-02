<script lang="ts">
	import { signIn, signOut } from '@auth/sveltekit/client';
	import { page } from '$app/stores';
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { redirectedOnce } from '$lib/stores/add-key-account-redirect';

	onMount(() => {
		if (!$redirectedOnce) {
			if ($page.data.session) {
				const email = $page.data.session.user?.email;
				if (email) {
					fetch('/api/users/validate', {
						method: 'POST',
						body: JSON.stringify({ email: email }),
						headers: {
							'Content-Type': 'application/json'
						}
					}).then((res) => {
						res.json().then((hasKey) => {
							if (!hasKey) {
								$redirectedOnce = true;
								goto('/account');
							}
						});
					});
				}
			}
		}
	});
</script>

<div class="login-buttons">
	{#if $page.data.session}
		<div class="logged-in-box">Logged in with {$page.data.session.user?.email}</div>
		<button title="Log out" on:click={() => signOut()}
			><i class="material-symbols-rounded">person_edit</i>Log out</button
		>
	{:else}
		<button title="Log in" on:click={() => signIn('google')}
			><i class="material-symbols-rounded">login</i>Log in</button
		>
	{/if}
</div>

<style>
	.logged-in-box {
		margin: 1em 0 0.5em 0;
		text-align: center;
		color: var(--text-color);
		font-weight: bold;
		text-shadow: 0px 4px 4px var(--shadow-color);
		cursor: default;
	}

	.login-buttons {
		display: flex;
		justify-content: center;
		flex-direction: column;
		width: 15em;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 4em;
		font-size: 1.25em;
	}

	@media screen and (max-width: 767px) {
		.logged-in-box {
			font-size: 1.5em;
		}

		.login-buttons {
			width: 12em;
		}
	}
</style>
