<script lang="ts">
	import Header from '$lib/components/global/Header.svelte';
	import Content from '$lib/components/global/Content.svelte';
	import GroupsTable from '$lib/components/groups-page/GroupsTable.svelte';
	import GroupsButtons from '$lib/components/groups-page/GroupsButtons.svelte';
	import LimitWarning from '$lib/components/global/LimitWarning.svelte';
	import { LIMIT_OF_GROUPS } from '$lib/stores/global';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let data;
	export let selectedGroupsToRemove: string[] = [];
</script>

<Header>
	<div class="title">
		<Tx text="your_groups"></Tx>
		<span title={$t('number_of_groups')} class:max={data.numGroups >= $LIMIT_OF_GROUPS}
			>[ {data.numGroups} / {$LIMIT_OF_GROUPS} ]</span
		>
	</div>
</Header>

<Content>
	<LimitWarning num={data.numGroups} limit={$LIMIT_OF_GROUPS} items="Groups" />
	<GroupsTable bind:groups={data.group_list} bind:selectedGroupsToRemove />
	<GroupsButtons
		bind:groups={data.group_list}
		users={data.user_list}
		numGroups={data.numGroups}
		bind:selectedGroupsToRemove
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
