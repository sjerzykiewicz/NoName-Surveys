<script lang="ts">
	import type { PageServerData } from './$types';

	export let data: PageServerData;
</script>

{#each data.survey_list as entry}
	<h1><a href="/{entry.survey_code}/summary">{entry.survey_code}</a></h1>
{/each}
