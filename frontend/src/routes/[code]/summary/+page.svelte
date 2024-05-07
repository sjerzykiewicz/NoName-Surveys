<script lang="ts">
	import type { PageServerData } from './$types';

	export let data: PageServerData;
</script>

{#each data.answers as survey}
	{survey.title}
{/each}
