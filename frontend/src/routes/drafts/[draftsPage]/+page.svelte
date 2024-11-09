<script lang="ts">
	import Header from '$lib/components/global/Header.svelte';
	import Content from '$lib/components/global/Content.svelte';
	import DraftsTable from '$lib/components/drafts-page/DraftsTable.svelte';
	import DraftsButtons from '$lib/components/drafts-page/DraftsButtons.svelte';
	import LimitWarning from '$lib/components/global/LimitWarning.svelte';
	import { LIMIT_OF_DRAFTS } from '$lib/stores/global';

	export let data;
	export let selectedDraftsToRemove: number[] = [];
</script>

<Header>
	<div class="title">
		Your drafts
		<span title="Number of drafts" class:max={data.numDrafts >= $LIMIT_OF_DRAFTS}
			>[ {data.numDrafts} / {$LIMIT_OF_DRAFTS} ]</span
		>
	</div>
</Header>

<Content>
	<LimitWarning num={data.numDrafts} limit={$LIMIT_OF_DRAFTS} items="Drafts" />
	<DraftsTable drafts={data.drafts.toReversed()} bind:selectedDraftsToRemove />
	<DraftsButtons
		drafts={data.drafts.toReversed()}
		numDrafts={data.numDrafts}
		bind:selectedDraftsToRemove
	/>
</Content>

<style>
	.title {
		display: flex;
		justify-content: space-between;
		white-space: normal !important;
	}

	.title span.max {
		color: var(--warning-color-1);
		transition:
			0.2s,
			outline 0s;
	}
</style>
