<script lang="ts">
	import type { PageServerData } from './$types';
	import SummaryEntry from '$lib/components/summary-page/SummaryEntry.svelte';
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';

	export let data: PageServerData;
</script>

<Header>
	<div class="header">Your surveys</div>
</Header>

<Content>
	{#each data.survey_list as entry}
		<SummaryEntry title={entry.title} code={entry.code} />
	{/each}
</Content>

<style>
	.header {
		text-shadow: 0px 4px 4px var(--box-shadow-color);
		font-size: 1.5em;
		font-weight: bold;
		font-family: 'Jura';
		color: var(--text-color);
	}

	@media screen and (max-width: 767px) {
		.header {
			font-size: 1.25em;
		}
	}
</style>
