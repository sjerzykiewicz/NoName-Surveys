<script lang="ts">
	import Header from '$lib/components/global/Header.svelte';
	import Content from '$lib/components/global/Content.svelte';
	import Footer from '$lib/components/global/Footer.svelte';
	import Back from '$lib/components/global/Back.svelte';
	import MembersTable from '$lib/components/groups-page/group/MembersTable.svelte';
	import MembersButtons from '$lib/components/groups-page/group/MembersButtons.svelte';
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';

	export let data;
	export let selectedMembersToRemove: string[] = [];

	$: notMembers = data.user_list.filter(
		(user) => !new Set(data.users.map((user) => user.email)).has(user)
	);
</script>

<Header>
	<div title="Group title" class="title">{data.group}</div>
</Header>

<Content>
	<MembersTable bind:members={data.users} bind:selectedMembersToRemove />
	<MembersButtons
		bind:members={data.users}
		{notMembers}
		group={data.group}
		numMembers={data.numMembers}
		bind:selectedMembersToRemove
	/>
</Content>

<Footer>
	<Back goBack={() => goto('/groups/' + $page.params.groupsPage)} />
</Footer>
