<script lang="ts">
	import { scale } from 'svelte/transition';

	let scrollHeight: number;

	$: showScrollToTop = scrollHeight > 100;
</script>

<svelte:window bind:scrollY={scrollHeight} />

{#if showScrollToTop}
	<button transition:scale on:click={() => window.scrollTo({ top: 0, behavior: 'smooth' })}>
		<i class="material-symbols-rounded">north</i>
	</button>
{/if}

<style>
	button {
		position: fixed;
		bottom: 0.75em;
		left: 1.5em;
		background-color: #4a4a4a;
		color: #eaeaea;
		border: none;
		border-radius: 5px;
		width: 3em;
		height: 3em;
		box-shadow: 0px 4px 4px #1a1a1a;
		cursor: pointer;
		transition-duration: 0.2s;
	}

	button:hover {
		transform: scale(120%);
	}

	button:active {
		background-color: #999999;
	}

	@media screen and (max-width: 767px) {
		button {
			bottom: 0.375em;
			left: 0.75em;
		}
	}
</style>
