<script lang="ts">
	import { title, questions, currentDraftId, draftStructure } from '$lib/stores/create-page';
	import Survey from '$lib/entities/surveys/Survey';
	import { SurveyError } from '$lib/entities/SurveyError';
	import { scrollToElementById } from '$lib/utils/scrollToElement';
	import { constructQuestionList } from '$lib/utils/constructQuestionList';
	import { popup } from '$lib/utils/popup';
	import DraftCreateInfo from '$lib/entities/surveys/DraftCreateInfo';
	import { getDraft } from '$lib/utils/getDraft';
	import { trimQuestions } from '$lib/utils/trimQuestions';
	import {
		errorModalContent,
		isErrorModalHidden,
		isWarningModalHidden,
		LIMIT_OF_CHARS,
		LIMIT_OF_DRAFTS,
		LIMIT_OF_SURVEYS,
		warningModalContent
	} from '$lib/stores/global';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import { invalidateAll } from '$app/navigation';
	import { checkQuestionError } from '$lib/utils/checkQuestionError';
	import Subtitle from './Subtitle.svelte';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let numSurveys: number;
	export let numDrafts: number;
	export let isPreview: boolean = false;
	export let isDraftModalHidden: boolean = true;
	export let isRespondentModalHidden: boolean = true;
	export let isExportButtonVisible: boolean = false;

	function togglePreview() {
		isPreview = !isPreview;
	}

	function checkCorrectness() {
		const t = $title.title;
		if (t === null || t === undefined || t.length === 0) {
			$title.error = SurveyError.TitleRequired;
		} else if (t.length > $LIMIT_OF_CHARS) {
			$title.error = SurveyError.TitleTooLong;
		} else {
			$title.error = SurveyError.NoError;
		}

		const numQuestions = $questions.length;

		for (let i = 0; i < numQuestions; i++) {
			checkQuestionError($questions[i], $LIMIT_OF_CHARS);
		}

		if ($title.error !== SurveyError.NoError) {
			scrollToElementById('header');
			return false;
		}

		if (!$questions.every((q) => q.error === SurveyError.NoError)) {
			scrollToElementById(
				`q${$questions.indexOf($questions.find((q) => q.error !== SurveyError.NoError)!).toString()}`
			);
			return false;
		}

		return true;
	}

	async function saveDraft() {
		if ($currentDraftId !== null) {
			$title.title = $title.title.trim();
			$questions = trimQuestions($questions);

			if (!checkCorrectness()) return;

			isDraftModalHidden = false;
		} else {
			if (numDrafts >= $LIMIT_OF_DRAFTS) {
				isExportButtonVisible = false;
				$warningModalContent = $t('limit_reached', { items: $t('drafts_genitive') });
				$isWarningModalHidden = false;
				return;
			}

			$title.title = $title.title.trim();
			$questions = trimQuestions($questions);

			if (!checkCorrectness()) return;

			const parsedSurvey = new Survey(constructQuestionList($questions));
			const draftInfo = new DraftCreateInfo($title.title, parsedSurvey);

			const response = await fetch('/api/surveys/drafts/create', {
				method: 'POST',
				body: JSON.stringify(draftInfo),
				headers: {
					'Content-Type': 'application/json'
				}
			});

			if (!response.ok) {
				const body = await response.json();
				$errorModalContent = getErrorMessage(body.detail);
				$isErrorModalHidden = false;
				return;
			}

			$currentDraftId = await response.json();
			$draftStructure = getDraft($title.title, $questions);
			popup('draft-popup');
			await invalidateAll();
		}
	}

	async function createSurvey() {
		if (numSurveys >= $LIMIT_OF_SURVEYS) {
			isExportButtonVisible = false;
			$warningModalContent = $t('limit_reached', { items: $t('surveys_genitive') });
			$isWarningModalHidden = false;
			return;
		}

		$title.title = $title.title.trim();
		$questions = trimQuestions($questions);

		if (!checkCorrectness()) return;

		isRespondentModalHidden = false;
	}
</script>

{#if isPreview}
	<button title={$t('edit_title')} class="footer-button" on:click={togglePreview}>
		<i class="symbol">edit</i><Tx text="edit" />
	</button>
{:else}
	<button
		title={$t('preview_title')}
		class="footer-button"
		on:click={() => {
			$title.title = $title.title.trim();
			$questions = trimQuestions($questions);
			togglePreview();
		}}
	>
		<i class="symbol">search</i><Tx text="preview" />
	</button>
{/if}
<div class="footer-button-group">
	<button
		title={$t('save_draft')}
		class="footer-button save popup"
		disabled={$questions.filter((q) => q.component != Subtitle).length === 0 || isPreview}
		on:click={saveDraft}
	>
		<i class="symbol">save</i><Tx text="save_draft" />
		<span class="popup-text top" id="draft-popup"><Tx text="saved" /></span>
	</button>
	<button
		title={$t('create_title')}
		class="footer-button done"
		id="create"
		disabled={$questions.filter((q) => q.component != Subtitle).length === 0 || isPreview}
		on:click={createSurvey}
	>
		<i class="symbol">done</i><Tx text="finish" />
	</button>
</div>

<style>
	.popup {
		--tooltip-width: 5em;
	}
</style>
