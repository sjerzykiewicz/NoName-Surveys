<script lang="ts">
	import { cubicInOut } from 'svelte/easing';
	import { scale } from 'svelte/transition';

	let scrollHeight: number;

	$: showScrollToTop = scrollHeight > 100;
</script>

<svelte:window bind:scrollY={scrollHeight} />

{#if showScrollToTop}
	<button
		class="scroll-to-top"
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
		left: 0.5em;
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

	@media screen and (max-width: 360px) {
		.scroll-to-top {
			bottom: 2.5em;
		}
	}
</style>
