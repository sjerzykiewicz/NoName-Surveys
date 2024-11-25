<script lang="ts">
	import amu from '$lib/assets/amu.png';
	import { startOAuth } from '$lib/utils/startOAuth';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);
</script>

<h1><Tx text="account_sign_in" /></h1>
<div class="sign-buttons">
	<button title={$t('sign_in')} class="sign-in" on:click={() => startOAuth('/account')}
		><img src={amu} alt="AMU logo" class="amu-logo" /><Tx text="sign_in" /></button
	>
</div>
<div title={$t('account_info_title')} class="info">
	<div class="text">
		<Tx html="account_authorization_info" />
	</div>
</div>
<div title={$t('account_info_title')} class="info bottom">
	<div class="text">
		<Tx text="account_info" />
	</div>
</div>

<style>
	h1 {
		text-align: center;
		text-shadow: 0px 4px 4px var(--shadow-color-1);
		color: var(--text-color-1);
		font-size: 2.75em;
		font-weight: 700;
		cursor: default;
		margin: 0;
		padding: 0.25em 0 0.5em;
		transition:
			0.2s,
			outline 0s;
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
		padding: 0.5em 0.5em 0em;
		border-top: 1px solid var(--border-color-1);
		text-shadow: 0px 4px 4px var(--shadow-color-1);
		cursor: default;
		overflow-wrap: break-word;
		color: var(--text-color-1);
		font-size: 1.1em;
		transition: 0.2s;
	}

	.info.bottom {
		padding: 0.5em;
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
		h1 {
			font-size: 2em;
		}

		.info {
			font-size: 0.8em;
			padding-left: 0em;
			padding-right: 0em;
		}
	}
</style>
