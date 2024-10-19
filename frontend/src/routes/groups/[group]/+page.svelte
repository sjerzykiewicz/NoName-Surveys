<script lang="ts">
	import type { PageServerData } from './$types';
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import Back from '$lib/components/Back.svelte';
	import UsersTable from '$lib/components/UsersTable.svelte';

	export let data: PageServerData;
</script>

<Header>
	<div title="Group title" class="title">{data.group}</div>
</Header>

<Content>
	<UsersTable users={data.users} title="Group Members" />
</Content>

<Footer>
	<Back />
</Footer>
