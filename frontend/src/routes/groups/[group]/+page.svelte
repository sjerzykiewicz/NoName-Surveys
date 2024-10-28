<script lang="ts">
	import type { PageData } from './$types';
	import Header from '$lib/components/global/Header.svelte';
	import Content from '$lib/components/global/Content.svelte';
	import Footer from '$lib/components/global/Footer.svelte';
	import Back from '$lib/components/global/Back.svelte';
	import MembersTable from '$lib/components/groups-page/group/MembersTable.svelte';
	import MembersButtons from '$lib/components/groups-page/group/MembersButtons.svelte';
	import { afterUpdate } from 'svelte';

	export let data: PageData;
	export let selectedMembersToRemove: string[] = [];

	let notMembers: string[] = [];

	afterUpdate(() => {
		notMembers = data.user_list.filter((user: string) => !data.users.includes(user));
	});
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
		bind:selectedMembersToRemove
	/>
</Content>

<Footer>
	<Back />
</Footer>
