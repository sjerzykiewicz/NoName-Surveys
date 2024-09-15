<script lang="ts">
	import type { LayoutServerData } from './$types';
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import GroupsTable from '$lib/components/groups-page/GroupsTable.svelte';

	export let data: LayoutServerData;
</script>

<Header>
	<div class="title">Your groups</div>
</Header>

<Content>
	<GroupsTable groups={data.group_list} />
</Content>
