<script lang="ts">
	import Header from '$lib/components/global/Header.svelte';
	import Content from '$lib/components/global/Content.svelte';
	import AnswersSummary from '$lib/components/summary-page/AnswersSummary.svelte';
	import Footer from '$lib/components/global/Footer.svelte';
	import Back from '$lib/components/global/Back.svelte';
	import AnswersTable from '$lib/components/summary-page/AnswersTable.svelte';
	import RespondentsTable from '$lib/components/summary-page/RespondentsTable.svelte';
	import ShareButton from '$lib/components/summary-page/ShareButton.svelte';
	import type { LayoutServerData } from './$types';
	import QrCodeModal from '$lib/components/global/QrCodeModal.svelte';
	import QrCodeButton from '$lib/components/summary-page/QrCodeButton.svelte';

	export let data: LayoutServerData;
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
	{#if data.answers.length === 0}
		<div title="Answers" class="title empty">No answers yet!</div>
	{:else}
		<AnswersSummary surveyAnswers={data.answers} />
		<AnswersTable {numbers} />
	{/if}
	{#if data.survey.uses_cryptographic_module}
		<RespondentsTable respondents={data.respondents} />
	{/if}
</Content>

<Footer>
	{#if data.answers.length > 0 && data.answers[0].is_owned_by_user}
		<ShareButton code={data.survey.survey_code} />
	{/if}
	<QrCodeButton bind:isModalHidden />
	<Back />
</Footer>
