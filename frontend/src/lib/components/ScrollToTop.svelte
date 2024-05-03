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
		bottom: 0.75em;
		left: 1.5em;
		background-color: var(--primary-dark-color);
		color: var(--text-color);
		border: none;
		border-radius: 5px;
		width: 3em;
		height: 3em;
		font-size: 0.8em;
		box-shadow: 0px 4px 4px var(--shadow-color);
		cursor: pointer;
		z-index: 5;
		transition: 0.2s;
	}

	.scroll-to-top:hover {
		transform: scale(120%);
	}

	.scroll-to-top:active {
		background-color: var(--border-color);
	}

	.material-symbols-rounded {
		font-size: 1.5em;
	}

	@media screen and (max-width: 767px) {
		.scroll-to-top {
			bottom: 0.375em;
			left: 0.75em;
		}
	}
</style>
