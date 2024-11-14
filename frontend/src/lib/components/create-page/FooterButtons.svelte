<script lang="ts">
	import { title, questions, currentDraftId, draftStructure } from '$lib/stores/create-page';
	import Survey from '$lib/entities/surveys/Survey';
	import Slider from '$lib/components/create-page/Slider.svelte';
	import Number from '$lib/components/create-page/Number.svelte';
	import Text from '$lib/components/create-page/Text.svelte';
	import Binary from '$lib/components/create-page/Binary.svelte';
	import { SurveyError } from '$lib/entities/SurveyError';
	import { scrollToElementById } from '$lib/utils/scrollToElement';
	import { tick } from 'svelte';
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

	async function checkCorrectness() {
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
			const q = $questions[i].question;
			if (q === null || q === undefined || q.length === 0) {
				$questions[i].error = SurveyError.QuestionRequired;
			} else if (q.length > $LIMIT_OF_CHARS) {
				$questions[i].error = SurveyError.QuestionTooLong;
			} else if (
				$questions[i].component != Text &&
				$questions[i].choices.some(
					(c) => c === null || c === undefined || c.toString().length === 0
				)
			) {
				switch ($questions[i].component) {
					case Number:
						$questions[i].error = SurveyError.NumberValuesRequired;
						break;
					case Slider:
						$questions[i].error = SurveyError.SliderValuesRequired;
						break;
					case Binary:
						$questions[i].error = SurveyError.BinaryChoicesRequired;
						break;
					default:
						$questions[i].error = SurveyError.ChoicesRequired;
				}
			} else if ($questions[i].choices.some((c) => c.length > $LIMIT_OF_CHARS)) {
				$questions[i].error = SurveyError.ChoicesTooLong;
			} else if (
				($questions[i].component === Slider || $questions[i].component === Number) &&
				parseFloat($questions[i].choices[0]) >= parseFloat($questions[i].choices[1])
			) {
				$questions[i].error = SurveyError.ImproperSliderValues;
			} else if (
				$questions[i].component === Slider &&
				parseFloat($questions[i].choices[2]) >
					parseFloat($questions[i].choices[1]) - parseFloat($questions[i].choices[0])
			) {
				$questions[i].error = SurveyError.ImproperSliderPrecision;
			} else if (
				$questions[i].component !== Slider &&
				new Set($questions[i].choices).size !== $questions[i].choices.length
			) {
				$questions[i].error = SurveyError.DuplicateChoices;
			} else {
				$questions[i].error = SurveyError.NoError;
			}
		}

		if ($title.error !== SurveyError.NoError) {
			await tick();
			scrollToElementById('header');
			return false;
		}

		if (!$questions.every((q) => q.error === SurveyError.NoError)) {
			await tick();
			scrollToElementById(
				$questions.indexOf($questions.find((q) => q.error !== SurveyError.NoError)!).toString()
			);
			return false;
		}

		return true;
	}

	async function saveDraft() {
		if ($currentDraftId !== null) {
			$title.title = $title.title.trim();
			$questions = trimQuestions($questions);

			if (!(await checkCorrectness())) return;

			isDraftModalHidden = false;
		} else {
			if (numDrafts >= $LIMIT_OF_DRAFTS) {
				isExportButtonVisible = false;
				$warningModalContent =
					'You have reached the maximum number of drafts you can create. Please delete some drafts to create new ones.';
				$isWarningModalHidden = false;
				return;
			}

			$title.title = $title.title.trim();
			$questions = trimQuestions($questions);

			if (!(await checkCorrectness())) return;

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
			$warningModalContent =
				'You have reached the maximum number of surveys you can create. Please delete some surveys to create new ones.';
			$isWarningModalHidden = false;
			return;
		}

		$title.title = $title.title.trim();
		$questions = trimQuestions($questions);

		if (!(await checkCorrectness())) return;

		isRespondentModalHidden = false;
	}
</script>

{#if isPreview}
	<button title={$t('footer_edit_t')} class="footer-button" on:click={togglePreview}>
		<i class="symbol">edit</i><Tx text="footer_edit"></Tx>
	</button>
{:else}
	<button
		title={$t('footer_preview')}
		class="footer-button"
		on:click={() => {
			$title.title = $title.title.trim();
			$questions = trimQuestions($questions);
			togglePreview();
		}}
	>
		<i class="symbol">search</i><Tx text="footer_preview"></Tx>
	</button>
{/if}
<div class="footer-button-group">
	<button
		title={$t('footer_save_draft')}
		class="footer-button save popup"
		disabled={$questions.length === 0 || isPreview}
		on:click={saveDraft}
	>
		<i class="symbol">save</i><Tx text="footer_save_draft"></Tx>
		<span class="popup-text top" id="draft-popup"><Tx text="footer_saved"></Tx></span>
	</button>
	<button
		title={$t('footer_create_t')}
		class="footer-button done"
		disabled={$questions.length === 0 || isPreview}
		on:click={createSurvey}
	>
		<i class="symbol">done</i><Tx text="footer_create"></Tx>
	</button>
</div>

<style>
	.popup {
		--tooltip-width: 5em;
	}
</style>
