<script lang="ts">
	import logo from '$lib/assets/uam_color_neg.svg';

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

<h1>Authorize yourself by AMU USOS:</h1>
<div class="sign-buttons">
	<button title="USOS" class="sign-in" on:click={startOAuth}
		><img src={logo} alt="amu_logo" class="amu-logo" /></button
	>
</div>
<div title="Account information" class="info">
	<div class="text">
		Authorizing yourself will enable you to:
		<ul>
			<li>
				<i class="material-symbols-rounded">chevron_right</i>Create both public and secure surveys,
			</li>
			<li>
				<i class="material-symbols-rounded">chevron_right</i>Save surveys as drafts for later
				editing,
			</li>
			<li>
				<i class="material-symbols-rounded">chevron_right</i>View responses and summaries of your
				surveys,
			</li>
			<li>
				<i class="material-symbols-rounded">chevron_right</i>Share surveys' results with others,
			</li>
			<li>
				<i class="material-symbols-rounded">chevron_right</i>Create and manage user groups,
			</li>
			<li>
				<i class="material-symbols-rounded">chevron_right</i>
				Generate digital signature keys that allow you to participate in secure surveys without needing
				to sign in each time.
			</li>
		</ul>
	</div>
</div>
<div title="Account information" class="info">
	<div class="text">
		We do not recommend signing in if you only wish to fill out a survey. For secure surveys, if you
		have already generated your digital signature keys, signing in is also not necessary.
	</div>
</div>

<style>
	ul {
		list-style-type: none;
		margin-top: 0.5em;
		padding-left: 1.5em;
	}

	li {
		display: flex;
		flex-flow: row nowrap;
		justify-content: flex-start;
		align-items: flex-start;
		padding-top: 0.5em;
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

	.sign-in {
		margin-left: 0.5em;
		margin-right: 0.5em;
	}

	.sign-in {
		font-size: 2em;
	}

	.info {
		font-size: 1.25em;
	}

	.amu-logo {
		height: 3em;
	}

	@media screen and (max-width: 768px) {
		h1 {
			font-size: 2em;
		}

		ul {
			padding-left: 0.5em;
		}
	}
</style>
