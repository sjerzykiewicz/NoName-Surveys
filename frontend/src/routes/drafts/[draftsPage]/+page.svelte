<script lang="ts">
	import type { PageServerData } from './$types';
	import Header from '$lib/components/global/Header.svelte';
	import Content from '$lib/components/global/Content.svelte';
	import DraftsTable from '$lib/components/drafts-page/DraftsTable.svelte';
	import { afterUpdate } from 'svelte';
	import { LIMIT_OF_DRAFTS } from '$lib/stores/global';
	import { slide } from 'svelte/transition';
	import { cubicInOut } from 'svelte/easing';

	export let data: PageServerData;

	let numDrafts: number = data.drafts.length;

	afterUpdate(() => {
		numDrafts = data.drafts.length;
	});
</script>

<Header>
	<div class="title">
		Your drafts
		<span title="Number of drafts" class:max={numDrafts >= $LIMIT_OF_DRAFTS}
			>[ {numDrafts} / {$LIMIT_OF_DRAFTS} ]</span
		>
	</div>
</Header>

<Content>
	{#if numDrafts >= $LIMIT_OF_DRAFTS}
		<p
			title="Draft limit reached"
			class="error"
			transition:slide={{ duration: 200, easing: cubicInOut }}
		>
			<i class="material-symbols-rounded">error</i>You have reached the maximum number of drafts.
			Please delete some drafts to create new ones.
		</p>
	{/if}
	<DraftsTable drafts={data.drafts.toReversed()} />
</Content>

<style>
	.title {
		display: flex;
		justify-content: space-between;
		white-space: normal !important;
	}

	.title span.max {
		color: var(--error-color);
	}

	.error {
		margin: 0em 0em 0.75em;
	}
</style>
