<script lang="ts">
	import Header from '$lib/components/global/Header.svelte';
	import Content from '$lib/components/global/Content.svelte';
	import Footer from '$lib/components/global/Footer.svelte';
	import SurveyTitle from '$lib/components/create-page/SurveyTitle.svelte';
	import SurveyTitlePreview from '$lib/components/create-page/preview/SurveyTitlePreview.svelte';
	import TitleError from '$lib/components/create-page/TitleError.svelte';
	import SurveyForm from '$lib/components/create-page/SurveyForm.svelte';
	import FooterButtons from '$lib/components/create-page/FooterButtons.svelte';
	import { beforeNavigate } from '$app/navigation';
	import { getDraft } from '$lib/utils/getDraft';
	import { trimQuestions } from '$lib/utils/trimQuestions';
	import { SurveyError } from '$lib/entities/SurveyError';
	import {
		title,
		questions,
		previousQuestion,
		useCrypto,
		ringMembers,
		selectedGroup,
		currentDraftId,
		draftStructure
	} from '$lib/stores/create-page';

	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let data;
	export let isPreview: boolean;
	export let isDraftModalHidden: boolean = true;
	export let isRespondentModalHidden: boolean = true;

	beforeNavigate((event) => {
		if (getDraft($title.title.trim(), trimQuestions($questions)) !== $draftStructure) {
			if (!confirm($t('info_about_leaving'))) {
				event.cancel();
				return;
			}
		}

		$title = { title: '', error: SurveyError.NoError };
		$questions = [];
		$previousQuestion = null;
		$useCrypto = false;
		$ringMembers = [];
		$selectedGroup = [];
		$currentDraftId = null;
		$draftStructure = getDraft('', []);
	});
</script>

<Header>
	{#if isPreview}
		<SurveyTitlePreview />
	{:else}
		<SurveyTitle />
		<TitleError />
	{/if}
</Header>
<Content>
	<SurveyForm
		{isPreview}
		groups={data.group_list}
		users={data.user_list}
		bind:isDraftModalHidden
		bind:isRespondentModalHidden
	/>
</Content>
<Footer>
	<FooterButtons bind:isPreview bind:isDraftModalHidden bind:isRespondentModalHidden />
</Footer>
