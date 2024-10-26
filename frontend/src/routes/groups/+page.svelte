<script lang="ts">
	import type { LayoutServerData } from './$types';
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import GroupsTable from '$lib/components/groups-page/GroupsTable.svelte';
	import GroupButtons from '$lib/components/groups-page/GroupButtons.svelte';
	import { afterUpdate } from 'svelte';
	import { LIMIT_OF_GROUPS } from '$lib/stores/global';
	import { slide } from 'svelte/transition';
	import { cubicInOut } from 'svelte/easing';

	export let data: LayoutServerData;
	export let selectedGroupsToRemove: string[] = [];

	let numGroups: number = data.group_list.length;

	afterUpdate(() => {
		numGroups = data.group_list.length;
	});
</script>

<Header>
	<div class="title">
		Your groups
		<span title="Number of groups" class:max={numGroups >= $LIMIT_OF_GROUPS}
			>[ {numGroups} / {$LIMIT_OF_GROUPS} ]</span
		>
	</div>
</Header>

<Content>
	{#if numGroups >= $LIMIT_OF_GROUPS}
		<p
			title="Group limit reached"
			class="error"
			transition:slide={{ duration: 200, easing: cubicInOut }}
		>
			<i class="material-symbols-rounded">error</i>You have reached the maximum number of groups.
			Please delete some groups to create new ones.
		</p>
	{/if}
	<GroupsTable bind:groups={data.group_list} bind:selectedGroupsToRemove />
	<GroupButtons bind:groups={data.group_list} users={data.user_list} bind:selectedGroupsToRemove />
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
