<script lang="ts">
	import Header from '$lib/components/global/Header.svelte';
	import Content from '$lib/components/global/Content.svelte';
	import GroupsTable from '$lib/components/groups-page/GroupsTable.svelte';
	import GroupsButtons from '$lib/components/groups-page/GroupsButtons.svelte';
	import LimitWarning from '$lib/components/global/LimitWarning.svelte';
	import { LIMIT_OF_GROUPS, S } from '$lib/stores/global';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let data;
	export let selectedGroupsToRemove: string[] = [];

	const groupLink =
		'https://github.com/sjerzykiewicz/NoName-Surveys?tab=readme-ov-file#create-a-user-group';

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

<Header>
	<div title={$t('your_groups')} class="title static">
		<div class="header-tooltip">
			<Tx text="your_groups" />
			<div class="tooltip hoverable">
				<i class="symbol">help</i>
				<span class="tooltip-text {innerWidth <= $S ? 'bottom' : 'right'}">
					<Tx text="groups_info" /><a href={groupLink} target="_blank"><Tx text="read_more" /></a>
				</span>
			</div>
		</div>
		<a
			href="/account/faq/#limit-items"
			title={$t('number_of_groups')}
			class="items"
			class:max={data.numGroups >= $LIMIT_OF_GROUPS}>[ {data.numGroups} / {$LIMIT_OF_GROUPS} ]</a
		>
	</div>
</Header>

<Content>
	<LimitWarning num={data.numGroups} limit={$LIMIT_OF_GROUPS} items={$t('groups_genitive')} />
	<GroupsTable bind:groups={data.group_list} bind:selectedGroupsToRemove />
	<GroupsButtons
		bind:groups={data.group_list}
		users={data.user_list}
		numGroups={data.numGroups}
		bind:selectedGroupsToRemove
	/>
</Content>

<style>
	.items {
		color: var(--text-color-1);
		opacity: 1;
		text-decoration: none;
		transition:
			0.2s,
			outline 0s;
	}

	.items:hover {
		opacity: 0.75;
	}

	.items.max {
		color: var(--warning-color-1);
	}
</style>
