<script lang="ts">
	import type { PageServerData } from './$types';
	import SummaryEntry from '$lib/components/summary-page/SummaryEntry.svelte';
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';

	export let data: PageServerData;
</script>

<Header>
	<div class="title">Your surveys</div>
</Header>

<Content>
	{#each data.survey_list as entry}
		<SummaryEntry title={entry.title} code={entry.code} />
	{/each}
</Content>
