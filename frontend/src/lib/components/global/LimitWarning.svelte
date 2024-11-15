<script lang="ts">
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import Tx from 'sveltekit-translate/translate/tx.svelte';

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
		<i class="symbol">warning</i><Tx text="limit_reached"></Tx>
		{items.toLowerCase()}.
		<Tx text="delete_some"></Tx>
		{items.toLowerCase()}
		<Tx text="to_create_new_ones"></Tx>.
	</p>
{/if}

<style>
	.warning {
		margin: 0em 0em 0.75em;
	}
</style>
