<script lang="ts">
	import Header from '$lib/components/global/Header.svelte';
	import Content from '$lib/components/global/Content.svelte';
	import Answers from '$lib/components/summary-page/answer/Answers.svelte';
	import Footer from '$lib/components/global/Footer.svelte';
	import Back from '$lib/components/global/Back.svelte';
	import ShareButton from '$lib/components/summary-page/buttons/ShareButton.svelte';
	import type { PageData } from './$types';
	import QrCodeModal from '$lib/components/global/QrCodeModal.svelte';
	import QrCodeButton from '$lib/components/summary-page/buttons/QrCodeButton.svelte';
	import { page } from '$app/stores';
	import AnswersButton from '$lib/components/summary-page/buttons/AnswersButton.svelte';
	import RespondentsButton from '$lib/components/summary-page/buttons/RespondentsButton.svelte';

	export let data: PageData;
	export let isModalHidden: boolean = true;

	let id: number = parseFloat($page.params.id);
</script>

<QrCodeModal
	bind:isHidden={isModalHidden}
	title="Access Code"
	surveyCode={data.survey.survey_code}
/>

<Header>
	<div class="title">{data.survey.title}</div>
</Header>

<Content>
	<Answers answer={data.answers[id]} {id} />
</Content>

<Footer>
	<!-- TODO: improve this -->
	{#if data.answers[id].is_owned_by_user}
		<ShareButton code={data.survey.survey_code} />
	{/if}
	{#if data.survey.uses_cryptographic_module}
		<RespondentsButton code={data.survey.survey_code} />
	{/if}
	<AnswersButton code={data.survey.survey_code} />
	<QrCodeButton bind:isModalHidden />
	<Back />
</Footer>
