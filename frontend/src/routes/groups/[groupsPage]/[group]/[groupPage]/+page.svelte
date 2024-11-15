<script lang="ts">
	import Header from '$lib/components/global/Header.svelte';
	import Content from '$lib/components/global/Content.svelte';
	import Footer from '$lib/components/global/Footer.svelte';
	import Back from '$lib/components/global/Back.svelte';
	import MembersTable from '$lib/components/groups-page/group/MembersTable.svelte';
	import MembersButtons from '$lib/components/groups-page/group/MembersButtons.svelte';
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let data;
	export let selectedMembersToRemove: string[] = [];
</script>

<Header>
	<div title={$t('group_title')} class="title">{data.group}</div>
</Header>

<Content>
	<MembersTable bind:members={data.members} bind:selectedMembersToRemove />
	<MembersButtons
		bind:members={data.members}
		notMembers={data.notMembers}
		group={data.group}
		numMembers={data.numMembers}
		bind:selectedMembersToRemove
	/>
</Content>

<Footer>
	<Back goBack={() => goto('/groups/' + $page.params.groupsPage)} />
</Footer>
