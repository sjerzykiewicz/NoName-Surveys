<script lang="ts">
	import { cubicInOut } from 'svelte/easing';
	import { scale } from 'svelte/transition';
	import { page } from '$app/stores';

	let scrollHeight: number;

	$: showScrollToTop = scrollHeight > 100;
</script>

<svelte:window bind:scrollY={scrollHeight} />

{#if showScrollToTop}
	<button
		class="scroll-to-top tooltip"
		class:create-page={$page.url.pathname === '/create'}
		class:fill-page={$page.url.pathname.startsWith('/fill')}
		transition:scale={{ duration: 200, easing: cubicInOut }}
		on:click={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
	>
		<i class="material-symbols-rounded">north</i>
		<span class="tooltip-text right">Scroll to the top.</span>
	</button>
{/if}

<style>
	.tooltip {
		--tooltip-width: 8em;
	}

	.tooltip .tooltip-text {
		font-size: 0.8em;
		background-color: var(--primary-dark-color);
	}

	.tooltip .tooltip-text::after {
		border-color: transparent var(--primary-dark-color) transparent transparent;
	}

	.scroll-to-top {
		position: fixed;
		justify-content: center;
		bottom: 0.25em;
		left: 0.25em;
		background-color: var(--primary-dark-color);
		border: none;
		font-size: 1.5em;
		z-index: 1;
		transition: 0.2s;
		cursor: pointer;
	}

	.scroll-to-top:hover {
		transform: scale(110%);
	}

	.scroll-to-top:active {
		background-color: var(--border-color);
	}

	@media screen and (max-width: 767px) {
		.tooltip .tooltip-text {
			font-size: 0.6em;
		}

		.scroll-to-top.fill-page {
			left: 0.5em;
			bottom: 0.5em;
		}
	}

	@media screen and (max-width: 355px) {
		.scroll-to-top.create-page {
			bottom: 2.5em;
		}
	}
</style>
