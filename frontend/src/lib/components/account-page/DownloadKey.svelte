<script lang="ts">
	import { L } from '$lib/stores/global';

	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';
	import formatDate from '$lib/utils/formatDate';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let isModalHidden: boolean = true;
	export let lastTime: string | null;

	$: timeDiff = lastTime !== null ? Date.now() - Date.parse(lastTime) : 0;
	function secondsToDays(seconds: number) {
		return (seconds / 3600 / 24).toFixed(0);
	}
	const WARNING_TRESHOLD = 335;

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

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
	<div class="last-update-info">
		<p><Tx text="account_last_key_update" />: {formatDate(lastTime)}</p>
		<div class="tooltip">
			<i class="symbol">info</i>
			<span class="tooltip-text {innerWidth <= $L ? 'bottom' : 'right'}">
				<Tx html="account_key_update_info" />
			</span>
		</div>
	</div>
	{#if secondsToDays(timeDiff) >= WARNING_TRESHOLD}
		<p title={$t('')} class="warning">
			<i class="symbol">warning</i>{$t('account_keys_expire_soon', {
				number: secondsToDays(timeDiff)
			})}
		</p>
	{/if}
{/if}

<style>
	.tooltip {
		--tooltip-width: 25em;
	}

	.tooltip i {
		font-size: 1.25em;
	}

	.download-key {
		display: flex;
		flex-direction: row;
		align-items: center;
		color: var(--text-color-1);
		font-size: 1.75em;
		width: fit-content;
		margin-inline: auto;
		padding-top: 1em;
		padding-bottom: 1.5em;
		border-bottom: 1px solid var(--border-color-1);
		transition:
			0.2s,
			outline 0s;
	}

	.download-key button {
		margin-right: 0.5em;
	}

	.download-key .tooltip .tooltip-text {
		font-size: 0.7em;
	}

	.last-update-info {
		display: flex;
		flex-direction: row;
		align-items: center;
	}

	.last-update-info {
		display: flex;
		flex-direction: row;
		align-items: center;
	}

	@media screen and (max-width: 1440px) {
		.tooltip {
			--tooltip-width: 14.5em;
		}
	}

	@media screen and (max-width: 1024px) {
		.tooltip {
			--tooltip-width: 17em;
		}
	}

	@media screen and (max-width: 768px) {
		.download-key {
			font-size: 1.25em;
		}

		.tooltip {
			--tooltip-width: 19em;
		}

		.tooltip .tooltip-text.bottom {
			left: unset;
			right: -15%;
			margin-left: 0em;
			margin-right: -1.15em;
		}

		.tooltip .tooltip-text.bottom::after {
			left: 91.5%;
			margin-left: -1.15em;
		}
	}
</style>
