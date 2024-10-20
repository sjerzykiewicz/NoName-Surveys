<script lang="ts">
	import type { PageServerData } from './$types';
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import Back from '$lib/components/Back.svelte';
	import MembersTable from '$lib/components/groups-page/group/MembersTable.svelte';

	export let data: PageServerData;
</script>

<Header>
	<div title="Group title" class="title">{data.group}</div>
</Header>

<Content>
	<MembersTable users={data.users} group={data.group} />
</Content>

<Footer>
	<Back />
</Footer>
