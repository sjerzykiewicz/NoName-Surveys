<script lang="ts">
	import type { PageData } from './$types';
	import Header from '$lib/components/global/Header.svelte';
	import Content from '$lib/components/global/Content.svelte';
	import Footer from '$lib/components/global/Footer.svelte';
	import Back from '$lib/components/global/Back.svelte';
	import QrCodeModal from '$lib/components/global/QrCodeModal.svelte';
	import QrCodeButton from '$lib/components/summary-page/buttons/QrCodeButton.svelte';
	import AnswersTable from '$lib/components/summary-page/answer/AnswersTable.svelte';
	import ShareButton from '$lib/components/summary-page/buttons/ShareButton.svelte';
	import RespondentsButton from '$lib/components/summary-page/buttons/RespondentsButton.svelte';
	import AnswersButton from '$lib/components/summary-page/buttons/AnswersButton.svelte';

	export let data: PageData;
	export let isModalHidden: boolean = true;

	let numbers: Array<number> = [];

	for (let i = 0; i < data.answers.length; i++) {
		numbers.push(i);
	}
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
	<AnswersTable {numbers} />
</Content>

<Footer>
	<!-- TODO: improve this -->
	{#if data.survey_list[data.survey_index].is_owned_by_user}
		<ShareButton />
	{/if}
	{#if data.survey.uses_cryptographic_module}
		<RespondentsButton />
	{/if}
	<AnswersButton />
	<QrCodeButton bind:isModalHidden />
	<Back />
</Footer>
