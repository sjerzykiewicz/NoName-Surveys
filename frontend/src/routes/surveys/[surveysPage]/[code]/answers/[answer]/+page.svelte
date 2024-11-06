<script lang="ts">
	import Header from '$lib/components/global/Header.svelte';
	import Content from '$lib/components/global/Content.svelte';
	import Answers from '$lib/components/summary-page/answer/Answers.svelte';
	import Footer from '$lib/components/global/Footer.svelte';
	import type { PageData } from './$types';
	import QrCodeModal from '$lib/components/global/QrCodeModal.svelte';
	import { page } from '$app/stores';
	import FooterButtons from '$lib/components/summary-page/buttons/FooterButtons.svelte';

	export let data: PageData;
	export let isModalHidden: boolean = true;

	let id: number = parseInt($page.params.answer);
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
	{#if !data.answers[id]}
		<div title="Answer no. {id + 1}" class="title empty">No {id + 1}. answer yet!</div>
	{:else}
		<Answers answer={data.answers[id]} {id} />
	{/if}
</Content>

<Footer>
	<FooterButtons
		isOwnedByUser={data.survey_list[data.survey_index].is_owned_by_user}
		usesCryptographicModule={data.survey.uses_cryptographic_module}
		bind:isModalHidden
	/>
</Footer>
