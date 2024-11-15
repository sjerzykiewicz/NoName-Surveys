<script lang="ts">
	import { page } from '$app/stores';
	import { M } from '$lib/stores/global';

	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';
	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let navLinks: Record<
		string,
		{ name: string; href: string; page: string; disabled: boolean }
	>;
	export let hideNav: () => void;

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

{#each Object.entries(navLinks) as [id, data]}
	<div
		title={data.disabled ? '' : $t(data.name)}
		{id}
		class="nav-link"
		class:tooltip={innerWidth > $M && data.disabled}
		class:disabled={data.disabled}
		class:active={$page.route.id === data.href ||
			$page.route.id === data.href + '/[' + data.name.toLowerCase() + 'Page]'}
	>
		<a href={data.disabled ? '' : data.href + data.page} on:click={hideNav}>{$t(data.name)}</a>
		{#if innerWidth > $M && data.disabled}
			<span class="tooltip-text bottom">
				<Tx text="sign_in_info" />
				<Tx text={data.name} />
			</span>
		{/if}
	</div>
{/each}

<style>
	.tooltip {
		--tooltip-width: 12.5em;
	}

	.tooltip .tooltip-text {
		font-size: 0.8em;
		font-weight: 400 !important;
		background-color: var(--primary-color-2);
	}

	.tooltip .tooltip-text.bottom::after {
		border-color: transparent transparent var(--primary-color-2) transparent;
	}

	.nav-link {
		display: flex;
		justify-content: center;
		align-items: center;
		text-align: center;
		color: var(--text-color-1);
		font-size: 1.5em;
		border-right: 1px solid var(--border-color-1);
		width: 100%;
		cursor: pointer;
		transition: background-color 0.2s;
	}

	.nav-link a {
		padding: 0.5em 0em;
		width: 100%;
		font-weight: 700 !important;
		color: inherit;
		text-decoration: none;
		cursor: inherit;
		transition: 0s;
	}

	.nav-link:hover {
		background-color: var(--primary-color-2);
	}

	.nav-link:active {
		background-color: var(--border-color-1);
	}

	.nav-link.active,
	.nav-link.active:hover {
		background-color: var(--accent-color-1);
		color: var(--text-color-2);
	}

	.nav-link.disabled,
	.nav-link.disabled:hover,
	.nav-link.disabled:active {
		cursor: not-allowed;
		color: var(--text-color-3);
		background-color: var(--secondary-color-1);
	}

	@media screen and (max-width: 768px) {
		.tooltip .tooltip-text {
			font-size: 0.6em;
		}

		.nav-link {
			border-top: 1px solid var(--border-color-1);
			border-right: none;
			border-bottom: none;
		}
	}
</style>
