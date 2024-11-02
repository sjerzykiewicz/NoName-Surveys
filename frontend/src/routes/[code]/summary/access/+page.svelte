<script lang="ts">
	import type { PageData } from './$types';
	import Header from '$lib/components/global/Header.svelte';
	import Content from '$lib/components/global/Content.svelte';
	import Footer from '$lib/components/global/Footer.svelte';
	import Back from '$lib/components/global/Back.svelte';
	import AccessTable from '$lib/components/summary-page/access/AccessTable.svelte';
	import UserButtons from '$lib/components/summary-page/access/UserButtons.svelte';
	import { afterUpdate } from 'svelte';
	import QrCodeModal from '$lib/components/global/QrCodeModal.svelte';
	import QrCodeButton from '$lib/components/summary-page/QrCodeButton.svelte';

	export let data: PageData;
	export let selectedUsersToRemove: string[] = [];
	export let isModalHidden: boolean = true;

	let usersWithoutAccess: string[] = [];

	afterUpdate(() => {
		const usersWithAccessSet = new Set(data.usersWithAccess);
		usersWithoutAccess = data.allUsers.filter((user) => !usersWithAccessSet.has(user));
	});
</script>

<QrCodeModal
	bind:isHidden={isModalHidden}
	title="Access Code"
	surveyCode={data.survey.survey_code}
/>

<Header>
	<div title="Survey title" class="title">{data.survey.title}</div>
</Header>

<Content>
	<AccessTable users={data.usersWithAccess} bind:selectedUsersToRemove />
	<UserButtons
		users={usersWithoutAccess}
		code={data.survey.survey_code}
		bind:selectedUsersToRemove
	/>
</Content>

<Footer>
	<QrCodeButton bind:isModalHidden />
	<Back />
</Footer>
