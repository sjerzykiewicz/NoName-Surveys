<script lang="ts">
	import Header from '$lib/components/global/Header.svelte';
	import Content from '$lib/components/global/Content.svelte';
	import Footer from '$lib/components/global/Footer.svelte';
	import Back from '$lib/components/global/Back.svelte';
	import AnswersSummary from '$lib/components/summary-page/AnswersSummary.svelte';
	import ImportSummaryButton from '$lib/components/global/ImportSummaryButton.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let data;
</script>

<Header>
	<div title={$t('survey_title')} class="title">
		{data.importedSummary?.[0]?.title ? data.importedSummary[0].title : $t('invalid_summary')}
	</div>
</Header>

<Content>
	{#if data.importedSummary?.[0]?.questions}
		<AnswersSummary surveyAnswers={data.importedSummary} isImported={true} />
	{/if}
</Content>

<Footer>
	<ImportSummaryButton />
	<Back />
</Footer>
