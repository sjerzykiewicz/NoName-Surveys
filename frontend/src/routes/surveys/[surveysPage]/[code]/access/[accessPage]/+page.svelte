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
	import QrCodeButton from '$lib/components/summary-page/buttons/QrCodeButton.svelte';
	import AnswersButton from '$lib/components/summary-page/buttons/AnswersButton.svelte';
	import RespondentsButton from '$lib/components/summary-page/buttons/RespondentsButton.svelte';
	import ShareButton from '$lib/components/summary-page/buttons/ShareButton.svelte';

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
	{#if data.usersWithAccess.length === 0}
		<div title="Users with access" class="title empty">No users with access to display!</div>
	{:else}
		<AccessTable users={data.usersWithAccess} bind:selectedUsersToRemove />
		<UserButtons
			users={usersWithoutAccess}
			code={data.survey.survey_code}
			bind:selectedUsersToRemove
		/>
	{/if}
</Content>

<Footer>
	<!-- TODO: improve this -->
	{#if data.survey_list[data.survey_index].is_owned_by_user}
		<ShareButton />
	{/if}
	{#if data.survey.uses_cryptographic_module}
		<RespondentsButton />
	{/if}
	<div class="footer-button-group">
		<AnswersButton />
		<div class="footer-button-group">
			<QrCodeButton bind:isModalHidden />
			<Back />
		</div>
	</div>
</Footer>
