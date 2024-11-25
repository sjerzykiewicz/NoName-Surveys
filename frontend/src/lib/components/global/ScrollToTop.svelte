<script lang="ts">
	import { cubicInOut } from 'svelte/easing';
	import { scale } from 'svelte/transition';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	let scrollHeight: number;

	$: showScrollToTop = scrollHeight > 100;
</script>

<svelte:window bind:scrollY={scrollHeight} />

{#if showScrollToTop}
	<button
		title={$t('scroll_to_top')}
		class="scroll-to-top"
		transition:scale={{ duration: 200, easing: cubicInOut }}
		on:click={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
	>
		<i class="symbol">north</i>
	</button>
{/if}

<style>
	.scroll-to-top {
		position: fixed;
		justify-content: center;
		bottom: 0.25em;
		left: 0.25em;
		background-color: var(--primary-color-1);
		border: none;
		border-radius: 50%;
		font-size: 1.5em;
		z-index: 1;
		cursor: pointer;
		transition:
			0.2s,
			outline 0s;
	}

	.scroll-to-top:hover {
		transform: scale(120%);
	}

	.scroll-to-top:active {
		background-color: var(--border-color-1);
	}

	@media screen and (max-width: 768px) {
		.scroll-to-top {
			bottom: 2.75em;
			left: 0;
			right: 0;
			width: fit-content;
			margin: auto;
		}
	}
</style>
