<script lang="ts">
	import type { PageData } from './$types';
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import Back from '$lib/components/Back.svelte';
	import UsersTable from '$lib/components/summary-page/access/UsersTable.svelte';

	export let data: PageData;
</script>

<Header>
	<div title="Survey title" class="title">{data.survey.survey_structure.title}</div>
</Header>

<Content>
	<UsersTable users={data.users} />
</Content>

<Footer>
	<Back />
</Footer>
