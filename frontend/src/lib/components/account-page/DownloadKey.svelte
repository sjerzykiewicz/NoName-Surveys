<script lang="ts">
	import { L } from '$lib/stores/global';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';
	import { formatDate } from '$lib/utils/formatDate';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let isModalHidden: boolean = true;
	export let lastTime: string | null;

	const ERROR_THRESHOLD = 365;
	const WARNING_THRESHOLD = 335;

	$: timeDiff = lastTime !== null ? secondsToDays(Date.now() - Date.parse(lastTime)) : 0;

	function secondsToDays(seconds: number) {
		return parseInt((seconds / 3600 / 24).toFixed(0));
	}

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

<div class="key-container">
	<div class="download-key">
		<button title={$t('account_new_key')} class="save" on:click={() => (isModalHidden = false)}>
			<i class="symbol">encrypted</i><Tx text="account_new_key" />
		</button>
		<div class="tooltip">
			<i class="symbol">info</i>
			<span class="tooltip-text {innerWidth <= $L ? 'bottom' : 'right'}">
				<Tx html="account_keys_info" />
			</span>
		</div>
	</div>
	{#if lastTime}
		<div class="last-update-container">
			<div title={$t('account_last_key_update')} class="last-update-info">
				<Tx text="account_last_key_update" />: {formatDate(lastTime)}
			</div>
			<div class="tooltip">
				<i class="symbol">info</i>
				<span class="tooltip-text {innerWidth <= $L ? 'bottom' : 'right'}">
					<Tx html="account_key_update_info" />
				</span>
			</div>
		</div>
		<div class="warning-div">
			{#if timeDiff >= ERROR_THRESHOLD}
				<p title={$t('account_expiration_critical')} class="error">
					<i class="symbol">error</i><Tx
						html="account_keys_expired"
						params={{ number: timeDiff }}
					/>
				</p>
			{:else if timeDiff >= WARNING_THRESHOLD}
				<p title={$t('account_expiration_warning')} class="warning">
					<i class="symbol">warning</i><Tx
						html="account_keys_expire_soon"
						params={{ number: timeDiff }}
					/>
				</p>
			{/if}
		</div>
	{/if}
</div>

<style>
	.tooltip i {
		font-size: 1.25em;
	}

	.key-container {
		display: flex;
		flex-direction: column;
		align-items: center;
		color: var(--text-color-1);
		width: fit-content;
		margin-inline: auto;
		padding-top: 1em;
		padding-bottom: 0.5em;
		font-size: 1.75em;
		border-bottom: 1px solid var(--border-color-1);
		transition:
			0.2s,
			outline 0s;
	}

	.download-key .tooltip {
		--tooltip-width: 25em;
	}

	.download-key .tooltip .tooltip-text {
		font-size: 0.7em;
	}

	.download-key {
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: flex-start;
		width: 100%;
		margin-inline: auto;
		padding-bottom: 0.5em;
	}

	.download-key button {
		margin-right: 0.5em;
	}

	.last-update-container {
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: flex-start;
		width: 100%;
		font-size: 0.8em;
		cursor: default;
	}

	.last-update-container .tooltip {
		--tooltip-width: 14em;
	}

	.last-update-container .tooltip .tooltip-text {
		font-size: 0.8em;
	}

	.last-update-info {
		margin-right: 0.5em;
		font-size: 0.8em;
	}

	.warning-div {
		display: flex;
		justify-content: flex-start;
		width: 100%;
	}

	.warning,
	.error {
		font-size: 0.5em;
	}

	.warning i,
	.error i {
		margin-right: 0.5em;
	}

	@media screen and (max-width: 1440px) {
		.download-key .tooltip {
			--tooltip-width: 14.5em;
		}
	}

	@media screen and (max-width: 1024px) {
		.download-key .tooltip {
			--tooltip-width: 17em;
		}
	}

	@media screen and (max-width: 768px) {
		.key-container {
			font-size: 1.25em;
		}

		.download-key .tooltip {
			--tooltip-width: 19em;
		}

		.download-key .tooltip .tooltip-text.bottom {
			left: -425%;
		}

		.download-key .tooltip .tooltip-text.bottom::after {
			left: 92.5%;
		}

		.last-update-container .tooltip .tooltip-text.bottom {
			left: -200%;
		}

		.last-update-container .tooltip .tooltip-text.bottom::after {
			left: 76%;
		}
	}
</style>
