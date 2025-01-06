<script lang="ts">
	import amu from '$lib/assets/amu.png';
	import { startOAuth } from '$lib/utils/startOAuth';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';
	import { M } from '$lib/stores/global';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	let isSignInButtonDisabled = false;

	const authLink =
		'https://github.com/sjerzykiewicz/NoName-Surveys?tab=readme-ov-file#-amu-usos-authentication';
	const readmeLink =
		'https://github.com/sjerzykiewicz/NoName-Surveys?tab=readme-ov-file#-noname-anonymous-surveys';

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

<h1><Tx text="account_sign_in" /></h1>
<div class="sign-buttons">
	<button
		title={$t('sign_in')}
		class="sign-in"
		disabled={isSignInButtonDisabled}
		on:click={async () => {
			isSignInButtonDisabled = true;
			await startOAuth('/account');
			isSignInButtonDisabled = false;
		}}><img src={amu} alt="AMU logo" class="amu-logo" /><Tx text="sign_in" /></button
	>
	<div class="tooltip hoverable">
		<i class="symbol">help</i>
		<span class="tooltip-text {innerWidth <= $M ? 'bottom' : 'right'}">
			<Tx text="auth_tooltip" />
			<a href={authLink} target="_blank"><Tx text="read_more" /></a>
		</span>
	</div>
</div>
<div title={$t('account_info_title')} class="info">
	<div class="text">
		<Tx html="account_authorization_info" />
	</div>
</div>
<div title={$t('account_info_title')} class="info bottom">
	<div class="text">
		<Tx text="account_info" /><a href={readmeLink} target="_blank"><Tx text="read_more" /></a>
	</div>
</div>

<style>
	.tooltip {
		--tooltip-width: 11em;
	}

	.tooltip .tooltip-text {
		font-size: 0.5em;
		text-align: left;
	}

	h1 {
		text-align: center;
		text-shadow: 0px 4px 4px var(--shadow-color-1);
		color: var(--text-color-1);
		font-size: 2.75em;
		font-weight: 700;
		cursor: default;
		margin: 0;
		padding: 0.25em 0 0.5em;
		transition: 0.2s;
	}

	.sign-buttons {
		display: flex;
		flex-flow: row;
		align-items: center;
		justify-content: center;
		font-size: 2em;
		margin-bottom: 1em;
		gap: 0.5em;
	}

	.info {
		display: flex;
		flex-flow: row;
		align-items: center;
		justify-content: flex-start;
		padding-top: 1em;
		padding-bottom: 1em;
		border-top: 1px solid var(--border-color-1);
		text-shadow: 0px 4px 4px var(--shadow-color-1);
		cursor: default;
		overflow-wrap: break-word;
		color: var(--text-color-1);
		font-size: 1.1em;
		transition: 0.2s;
	}

	.info.bottom {
		border-bottom: 1px solid var(--border-color-1);
	}

	.text {
		font-weight: 700;
		text-align: left;
	}

	.info.bottom .text {
		font-weight: 500;
	}

	@media screen and (max-width: 768px) {
		.tooltip {
			font-size: 0.8em;
		}

		h1 {
			font-size: 2em;
		}

		.sign-buttons {
			flex-flow: column;
			margin-bottom: 0.25em;
		}

		.info {
			font-size: 0.8em;
			padding-left: 0em;
			padding-right: 0em;
		}
	}
</style>
