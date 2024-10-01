<script lang="ts">
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import SurveyTitle from '$lib/components/create-page/SurveyTitle.svelte';
	import SurveyTitlePreview from '$lib/components/create-page/preview/SurveyTitlePreview.svelte';
	import TitleError from '$lib/components/create-page/TitleError.svelte';
	import SurveyForm from '$lib/components/create-page/SurveyForm.svelte';
	import FooterButtons from '$lib/components/create-page/FooterButtons.svelte';
	import type { PageServerData } from './$types';
	import { beforeNavigate } from '$app/navigation';
	import { getDraftHash } from '$lib/utils/getDraftHash';
	import {
		title,
		questions,
		previousQuestion,
		useCrypto,
		ringMembers,
		selectedGroup,
		currentDraftId,
		draftHash
	} from '$lib/stores/create-page';

	export let titleError: boolean;
	export let cryptoError: boolean;
	export let isPreview: boolean;
	export let data: PageServerData;

	beforeNavigate((event) => {
		if (getDraftHash($title, $questions) !== $draftHash) {
			if (
				!confirm(
					'Are you sure you want to leave this page?\nLeaving will discard all unsaved changes.'
				)
			) {
				event.cancel();
				return;
			}
		}

		$title = '';
		$questions = [];
		$previousQuestion = null;
		$useCrypto = false;
		$ringMembers = [];
		$selectedGroup = [];
		$currentDraftId = null;
		$draftHash = getDraftHash('', []);
	});
</script>

<Header>
	{#if isPreview}
		<SurveyTitlePreview />
	{:else}
		<SurveyTitle />
		<TitleError {titleError} />
	{/if}
</Header>
<Content>
	<SurveyForm {cryptoError} {isPreview} groups={data.group_list} users={data.user_list} />
</Content>
<Footer>
	<FooterButtons bind:titleError bind:cryptoError bind:isPreview />
</Footer>
