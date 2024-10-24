<script lang="ts">
	import Tx from 'sveltekit-translate/translate/tx.svelte';

	import amu from '$lib/assets/amu.png';

	async function startOAuth() {
		try {
			const response = await fetch('/api/oauth/request-token', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				}
			});

			const data = await response.json();

			const expires = new Date(Date.now() + 3 * 60 * 1000).toUTCString();
			document.cookie = `oauth_token_secret=${data.oauth_token_secret}; path=/; secure; expires=${expires}`;

			if (data.oauth_token) {
				window.location.href = `/auth/redirect?oauth_token=${data.oauth_token}`;
			} else {
				console.error('Failed to get OAuth token');
			}
		} catch (error) {
			console.error('OAuth request failed:', error);
		}
	}
</script>

<h1><Tx text="account_sign_in"></Tx></h1>
<div class="sign-buttons">
	<button title="AMU USOS" class="sign-in" on:click={startOAuth}
		><img src={amu} alt="AMU logo" class="amu-logo" /><Tx text="sign_in"></Tx></button
	>
</div>
<div title="Account information" class="info">
	<div class="text">
		<Tx html="account_authorization_info"></Tx>
	</div>
</div>
<div title="Account information" class="info">
	<div class="text">
		<Tx text="account_info"></Tx>
	</div>
</div>

<!-- TODO: Make it better!-->
<!-- Placeholder to ensure ul/li CSS styles are used -->
{#if false}
	<ul class="icon accent">
		<li></li>
	</ul>
{/if}

<style>
	ul {
		list-style-type: none;
		margin-top: 0.25em;
		padding-left: 1.5em;
	}

	li {
		display: flex;
		flex-flow: row nowrap;
		justify-content: flex-start;
		align-items: flex-start;
		padding-top: 0.75em;
	}

	.icon {
		margin-right: 0.5em;
	}

	h1 {
		text-align: center;
		text-shadow: 0px 4px 4px var(--shadow-color);
		color: var(--text-color);
		font-size: 3em;
		font-weight: bold;
		cursor: default;
		margin: 0;
		padding: 0.25em 0 0.5em;
	}

	.sign-buttons {
		display: flex;
		flex-flow: row;
		align-items: center;
		justify-content: center;
		margin-bottom: 2em;
	}

	.info {
		display: flex;
		flex-flow: row;
		align-items: center;
		justify-content: center;
		padding: 1.25em 0.5em 0em;
		border-top: 1px solid var(--border-color);
		text-shadow: 0px 4px 4px var(--shadow-color);
		cursor: default;
		overflow-wrap: break-word;
		color: var(--text-color);
		font-size: 1.25em;
	}

	.text {
		text-align: justify;
	}

	.accent {
		color: var(--accent-color);
		font-weight: 700;
	}

	@media screen and (max-width: 768px) {
		h1 {
			font-size: 2em;
		}

		ul {
			padding-left: 0.5em;
		}

		.info {
			font-size: 1em;
			padding-left: 0em;
			padding-right: 0em;
		}
	}
</style>
