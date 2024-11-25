<script lang="ts">
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let num: number;
	export let limit: number;
	export let items: string;
</script>

{#if num >= limit}
	<p
		title={$t('limit_reached_title', { items: items })}
		class="warning"
		transition:slide={{ duration: 200, easing: cubicInOut }}
	>
		<i class="symbol">warning</i>{$t('limit_reached', { items: items.toLowerCase() })}.
	</p>
{/if}

<style>
	.warning {
		margin: 0em 0em 0.75em;
	}
</style>
