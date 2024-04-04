<script lang="ts">
	import type { PageData } from './$types';

	export let data: PageData;
</script>

{#if data.message}
	<h1>{data.message}</h1>
{:else}
	<h1>Loading...</h1>
{/if}
