<script lang="ts">
	import Header from '$lib/components/global/Header.svelte';
	import Content from '$lib/components/global/Content.svelte';
	import Footer from '$lib/components/global/Footer.svelte';
	import AccessTable from '$lib/components/summary-page/access/AccessTable.svelte';
	import UserButtons from '$lib/components/summary-page/access/UserButtons.svelte';
	import { afterUpdate } from 'svelte';
	import QrCodeModal from '$lib/components/global/QrCodeModal.svelte';
	import FooterButtons from '$lib/components/summary-page/buttons/FooterButtons.svelte';

	export let data;
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
	{#if data.usersWithAccess.length === 0}
		<div title="Users with access" class="title empty">No users with access to display!</div>
	{:else}
		<AccessTable users={data.usersWithAccess} bind:selectedUsersToRemove />
		<UserButtons
			users={usersWithoutAccess}
			code={data.survey.survey_code}
			numUsers={data.numUsers}
			bind:selectedUsersToRemove
		/>
	{/if}
</Content>

<Footer>
	<FooterButtons
		isOwnedByUser={data.survey_list[data.survey_index].is_owned_by_user}
		usesCryptographicModule={data.survey.uses_cryptographic_module}
		bind:isModalHidden
	/>
</Footer>
