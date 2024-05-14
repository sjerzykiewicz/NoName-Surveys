<script lang="ts">
	import type { PageServerData } from '../$types';
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import Entry from '$lib/components/draft-page/Entry.svelte';

	export let data: PageServerData;
</script>

<Header>
	<div class="title">Your drafts</div>
</Header>

<Content>
	{#each data.drafts as draft}
		<Entry structure={draft.survey_structure} creationDate={draft.creation_date} />
	{/each}
</Content>
