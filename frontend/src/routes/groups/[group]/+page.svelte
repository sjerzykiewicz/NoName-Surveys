<script lang="ts">
	import type { PageServerData } from './$types';
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import UsersTable from '$lib/components/groups-page/group/UsersTable.svelte';

	export let data: PageServerData;
</script>

<Header>
	<div class="title">{data.group}</div>
</Header>

<Content>
	<UsersTable users={data.users} />
</Content>

<Footer>
	<button
		title="Go back"
		class="footer-button"
		on:click={() => {
			history.back();
		}}><i class="material-symbols-rounded">undo</i>Back</button
	>
</Footer>
