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
		title="Scroll to the top of the page"
		class="scroll-to-top"
		class:create-page={$page.url.pathname === '/create'}
		class:fill-page={$page.url.pathname.startsWith('/fill')}
		transition:scale={{ duration: 200, easing: cubicInOut }}
		on:click={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
	>
		<i class="material-symbols-rounded">north</i>
	</button>
{/if}

<style>
	.scroll-to-top {
		position: fixed;
		justify-content: center;
		bottom: 0.25em;
		left: 0.25em;
		background-color: var(--primary-dark-color);
		border: none;
		font-size: 1.5em;
		z-index: 5;
		transition: 0.2s;
	}

	.scroll-to-top:hover {
		transform: scale(110%);
	}

	.scroll-to-top:active {
		background-color: var(--border-color);
	}

	@media screen and (max-width: 767px) {
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
