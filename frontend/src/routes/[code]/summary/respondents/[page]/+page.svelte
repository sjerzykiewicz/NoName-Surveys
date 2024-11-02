<script lang="ts">
	import type { PageData } from './$types';
	import Header from '$lib/components/global/Header.svelte';
	import Content from '$lib/components/global/Content.svelte';
	import Footer from '$lib/components/global/Footer.svelte';
	import Back from '$lib/components/global/Back.svelte';
	import QrCodeModal from '$lib/components/global/QrCodeModal.svelte';
	import QrCodeButton from '$lib/components/summary-page/buttons/QrCodeButton.svelte';
	import RespondentsTable from '$lib/components/summary-page/respondents/RespondentsTable.svelte';
	import ShareButton from '$lib/components/summary-page/buttons/ShareButton.svelte';
	import AnswersButton from '$lib/components/summary-page/buttons/AnswersButton.svelte';

	export let data: PageData;
	export let isModalHidden: boolean = true;
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
	<RespondentsTable respondents={data.respondents} />
</Content>

<Footer>
	<!-- TODO: improve this -->
	{#if data.answers.length > 0 && data.answers[0].is_owned_by_user}
		<ShareButton code={data.survey.survey_code} />
	{/if}
	{#if data.answers.length > 0}
		<AnswersButton code={data.survey.survey_code} />
	{/if}
	<QrCodeButton bind:isModalHidden />
	<Back />
</Footer>
