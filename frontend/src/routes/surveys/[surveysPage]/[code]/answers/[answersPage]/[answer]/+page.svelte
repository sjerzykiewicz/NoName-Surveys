<script lang="ts">
	import Header from '$lib/components/global/Header.svelte';
	import Content from '$lib/components/global/Content.svelte';
	import Answers from '$lib/components/summary-page/answer/Answers.svelte';
	import Footer from '$lib/components/global/Footer.svelte';
	import QrCodeModal from '$lib/components/global/QrCodeModal.svelte';
	import { page } from '$app/stores';
	import FooterButtons from '$lib/components/summary-page/buttons/FooterButtons.svelte';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let data;
	export let isModalHidden: boolean = true;

	let id: number = parseInt($page.params.answer);
</script>

<QrCodeModal
	bind:isHidden={isModalHidden}
	title={$t('access_code')}
	surveyCode={data.survey.survey_code}
/>

<Header>
	<div class="title">{data.survey.title}</div>
</Header>

<Content>
	{#if !data.answers[id]}
		<div title={$t('answer_no', { index: id + 1 })} class="title empty">
			<Tx text="no_answer_yet" params={{ index: id + 1 }} />
		</div>
	{:else}
		<Answers answer={data.answers[id]} {id} />
	{/if}
</Content>

<Footer>
	<FooterButtons
		isOwnedByUser={data.surveys[data.survey_index].is_owned_by_user}
		usesCryptographicModule={data.survey.uses_cryptographic_module}
		bind:isModalHidden
	/>
</Footer>
