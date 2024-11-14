<script lang="ts">
	import Header from '$lib/components/global/Header.svelte';
	import Content from '$lib/components/global/Content.svelte';
	import Footer from '$lib/components/global/Footer.svelte';
	import QrCodeModal from '$lib/components/global/QrCodeModal.svelte';
	import AnswersTable from '$lib/components/summary-page/answer/AnswersTable.svelte';
	import FooterButtons from '$lib/components/summary-page/buttons/FooterButtons.svelte';
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let data;
	export let isModalHidden: boolean = true;

	let numbers: Array<number> = [];

	for (let i = 0; i < data.answers.length; i++) {
		numbers.push(i);
	}
</script>

<QrCodeModal
	bind:isHidden={isModalHidden}
	title={$t('access_code')}
	surveyCode={data.survey.survey_code}
/>

<Header>
	<div title={$t('survey_title')} class="title">{data.survey.title}</div>
</Header>

<Content>
	<AnswersTable {numbers} />
</Content>

<Footer>
	<FooterButtons
		isOwnedByUser={data.surveys[data.survey_index].is_owned_by_user}
		usesCryptographicModule={data.survey.uses_cryptographic_module}
		goBack={() => goto('/surveys/' + $page.params.surveysPage)}
		bind:isModalHidden
	/>
</Footer>
