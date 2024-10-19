<script lang="ts">
	import type { PageData } from './$types';
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import Back from '$lib/components/Back.svelte';
	import AccessTable from '$lib/components/summary-page/access/AccessTable.svelte';
	import AddUserButtons from '$lib/components/summary-page/access/AddUserButtons.svelte';
	import { afterUpdate } from 'svelte';

	export let data: PageData;

	let usersWithoutAccess: string[] = [];

	afterUpdate(() => {
		usersWithoutAccess = data.allUsers.filter(
			(user: string) => !data.usersWithAccess.includes(user)
		);
	});
</script>

<Header>
	<div title="Survey title" class="title">{data.survey.survey_structure.title}</div>
</Header>

<Content>
	<AccessTable users={data.usersWithAccess} code={data.code} />
	<AddUserButtons users={usersWithoutAccess} code={data.code} />
</Content>

<Footer>
	<Back />
</Footer>
