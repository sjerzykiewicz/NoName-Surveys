<script lang="ts">
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	export let num: number;
	export let limit: number;
	export let items: string;
</script>

{#if num >= limit}
	<p
		title="{items} limit reached"
		class="warning"
		transition:slide={{ duration: 200, easing: cubicInOut }}
	>
		<i class="material-symbols-rounded">warning</i>You have reached the maximum number of {items.toLowerCase()}.
		Please delete some {items.toLowerCase()} to create new ones.
	</p>
{/if}

<style>
	.warning {
		margin: 0em 0em 0.75em;
	}
</style>
