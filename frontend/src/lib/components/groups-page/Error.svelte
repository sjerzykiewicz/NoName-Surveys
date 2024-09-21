<script lang="ts">
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	export let id: string;
	export let data: string | string[];
	export let error: boolean;
	export let message: string;

	$: checkError = () => {
		return error && (data === null || data === undefined || data.length === 0);
	};
</script>

<div
	in:slide={{ delay: 200, duration: 200, easing: cubicInOut }}
	out:slide={{ duration: 200, easing: cubicInOut }}
>
	{#if checkError()}
		<p title="Error" class="error" {id} transition:slide={{ duration: 200, easing: cubicInOut }}>
			<i class="material-symbols-rounded">error</i>{message}
		</p>
	{/if}
</div>

<style>
	#name {
		margin-left: 6.6em;
	}
</style>
