<script lang="ts">
	import { M } from '$lib/stores/global';

	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let isModalHidden: boolean = true;

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

<div class="download-key">
	<button title={$t('account_new_key')} class="save" on:click={() => (isModalHidden = false)}>
		<i class="material-symbols-rounded">encrypted</i><Tx text="account_new_key"></Tx>
	</button>
	<div class="tooltip">
		<i class="material-symbols-rounded">info</i>
		<span class="tooltip-text {innerWidth <= $M ? 'bottom' : 'right'}">
			<Tx html="account_keys_info"></Tx>
		</span>
	</div>
</div>

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
		color: var(--text-color);
		font-size: 1.5em;
		width: fit-content;
		margin-inline: auto;
		padding-top: 1em;
		padding-bottom: 1.5em;
		border-bottom: 1px solid var(--border-color);
	}

	.download-key button {
		margin-right: 0.5em;
	}

	@media screen and (max-width: 1440px) {
		.tooltip {
			--tooltip-width: 17em;
		}
	}

	@media screen and (max-width: 1024px) {
		.tooltip {
			--tooltip-width: 9.5em;
		}
	}

	@media screen and (max-width: 768px) {
		.download-key {
			font-size: 1.25em;
		}

		.tooltip {
			--tooltip-width: 18em;
		}

		.tooltip .tooltip-text.bottom {
			left: unset;
			right: -25%;
			margin-left: 0em;
			margin-right: -1.15em;
		}

		.tooltip .tooltip-text.bottom::after {
			left: 91.5%;
			margin-left: -1.15em;
		}
	}
</style>
