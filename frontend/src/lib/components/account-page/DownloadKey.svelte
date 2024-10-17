<script lang="ts">
	import { M } from '$lib/stores/global';

	export let isModalHidden: boolean = true;

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

<div class="download-key">
	<button title="Generate new keys" class="save" on:click={() => (isModalHidden = false)}>
		<i class="material-symbols-rounded">encrypted</i>Generate New Keys
	</button>
	<div class="tooltip">
		<i class="material-symbols-rounded">info</i>
		<span class="tooltip-text {innerWidth <= $M ? 'bottom' : 'right'}">
			These keys allow you to participate in secure surveys. Once they are generated, it is your
			responsibility to keep them safe. When submitting a secure survey, you will be asked to
			provide these keys to your browser for digital signature.
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
		text-shadow: 0px 4px 4px var(--shadow-color);
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
