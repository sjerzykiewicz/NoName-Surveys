<script lang="ts">
	import { scale } from 'svelte/transition';

	let scrollHeight: number;

	$: showScrollToTop = scrollHeight > 100;
</script>

<svelte:window bind:scrollY={scrollHeight} />

{#if showScrollToTop}
	<button
		class="scroll-to-top"
		transition:scale
		on:click={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
	>
		<i class="material-symbols-rounded">arrow_upward</i>
	</button>
{/if}

<style>
	.scroll-to-top {
		position: fixed;
		bottom: 0.7em;
		left: 2em;
		background-color: #4a4a4a;
		color: white;
		border: none;
		border-radius: 25%;
		width: 3em;
		height: 3em;
		box-shadow: 0px 4px 4px #1a1a1a;
		z-index: 5;
		transition-duration: 0.2s;
	}

	.scroll-to-top:hover {
		transform: translateY(-10px);
	}

	@media screen and (max-width: 767px) {
		.scroll-to-top {
			bottom: 0.5em;
			left: 1em;
		}
	}
</style>
