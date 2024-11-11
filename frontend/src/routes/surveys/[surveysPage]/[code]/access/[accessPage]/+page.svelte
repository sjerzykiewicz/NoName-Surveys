<script lang="ts">
	import Header from '$lib/components/global/Header.svelte';
	import Content from '$lib/components/global/Content.svelte';
	import Footer from '$lib/components/global/Footer.svelte';
	import AccessTable from '$lib/components/summary-page/access/AccessTable.svelte';
	import UserButtons from '$lib/components/summary-page/access/UserButtons.svelte';
	import QrCodeModal from '$lib/components/global/QrCodeModal.svelte';
	import FooterButtons from '$lib/components/summary-page/buttons/FooterButtons.svelte';
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';

	export let data;
	export let selectedUsersToRemove: string[] = [];
	export let isModalHidden: boolean = true;

	$: usersWithoutAccess = data.allUsers.filter((user) => !new Set(data.usersWithAccess).has(user));
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
		{usersWithoutAccess}
		usersWithAccess={data.usersWithAccess}
		code={data.survey.survey_code}
		numUsers={data.numUsers}
		bind:selectedUsersToRemove
	/>
</Content>

<Footer>
	<FooterButtons
		isOwnedByUser={data.surveys[data.survey_index].is_owned_by_user}
		usesCryptographicModule={data.survey.uses_cryptographic_module}
		goBack={() => goto('/surveys/' + $page.params.surveysPage)}
		bind:isModalHidden
	/>
</Footer>
