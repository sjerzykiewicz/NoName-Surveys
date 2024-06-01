<script lang="ts">
	import type { PageServerData } from './$types';
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import DraftsTable from '$lib/components/drafts-page/DraftsTable.svelte';

	export let data: PageServerData;
</script>

<Header>
	<div class="title">Your drafts</div>
</Header>

<Content>
	<DraftsTable drafts={data.drafts.toReversed()} />
</Content>
