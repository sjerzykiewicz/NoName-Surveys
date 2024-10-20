<script lang="ts">
	import {
		title,
		questions,
		useCrypto,
		ringMembers,
		selectedGroup,
		currentDraftId,
		draftStructure
	} from '$lib/stores/create-page';
	import Survey from '$lib/entities/surveys/Survey';
	import Slider from '$lib/components/create-page/Slider.svelte';
	import Number from '$lib/components/create-page/Number.svelte';
	import Text from '$lib/components/create-page/Text.svelte';
	import Binary from '$lib/components/create-page/Binary.svelte';
	import SurveyInfo from '$lib/entities/surveys/SurveyCreateInfo';
	import { SurveyError } from '$lib/entities/SurveyError';
	import { scrollToElementById } from '$lib/utils/scrollToElement';
	import { tick } from 'svelte';
	import { page } from '$app/stores';
	import { constructQuestionList } from '$lib/utils/constructQuestionList';
	import { popup } from '$lib/utils/popup';
	import DraftCreateInfo from '$lib/entities/surveys/DraftCreateInfo';
	import { getDraft } from '$lib/utils/getDraft';
	import { trimQuestions } from '$lib/utils/trimQuestions';
	import { LIMIT_OF_CHARS } from '$lib/stores/global';

	export let isPreview: boolean = false;
	export let cryptoError: boolean = false;
	export let isDraftModalHidden: boolean = true;
	export let isSurveyModalHidden: boolean = true;
	export let surveyCode: string;

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
				$questions[i].choices.some((c) => c === null || c === undefined || c.length === 0)
			) {
				switch ($questions[i].component) {
					case Slider:
					case Number:
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
			} else if (new Set($questions[i].choices).size !== $questions[i].choices.length) {
				$questions[i].error = SurveyError.DuplicateChoices;
			} else {
				$questions[i].error = SurveyError.NoError;
			}
		}

		cryptoError = false;
		const g = $selectedGroup;
		const r = $ringMembers;
		if (
			$useCrypto &&
			(g === null || g === undefined || g.length === 0) &&
			(r === null || r === undefined || r.length === 0)
		) {
			cryptoError = true;
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

		if (cryptoError) {
			await tick();
			scrollToElementById('crypto');
			return false;
		}

		return true;
	}

	async function saveDraft() {
		$title.title = $title.title.trim();
		$questions = trimQuestions($questions);

		if (!(await checkCorrectness())) return;

		if ($currentDraftId !== null) {
			isDraftModalHidden = false;
		} else {
			const parsedSurvey = new Survey($title.title, constructQuestionList($questions));
			const draftInfo = new DraftCreateInfo($page.data.session!.user!.email!, parsedSurvey);

			const response = await fetch('/api/surveys/drafts/create', {
				method: 'POST',
				body: JSON.stringify(draftInfo),
				headers: {
					'Content-Type': 'application/json'
				}
			});

			if (!response.ok) {
				const body = await response.json();
				alert(body.detail);
				return;
			}

			$currentDraftId = await response.json();
			$draftStructure = getDraft($title.title, $questions);
			popup('draft-popup');
		}
	}

	let ring: string[] = [];

	async function fetchGroup(name: string) {
		const response = await fetch('/api/groups/fetch', {
			method: 'POST',
			body: JSON.stringify({ user_email: $page.data.session?.user?.email, name: name }),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (!response.ok) {
			const body = await response.json();
			alert(body.detail);
			return;
		}

		const body = await response.json();
		ring = [...$ringMembers, ...body];
	}

	async function createSurvey() {
		$title.title = $title.title.trim();
		$questions = trimQuestions($questions);

		if (!(await checkCorrectness())) return;

		const parsedSurvey = new Survey($title.title, constructQuestionList($questions));
		let finalRing: string[] = [];

		if ($selectedGroup.length > 0) {
			await fetchGroup($selectedGroup[0]);
			finalRing = [...new Set(ring)];
		} else if ($ringMembers.length > 0) {
			finalRing = [...$ringMembers];
		}

		const surveyInfo = new SurveyInfo(
			$page.data.session!.user!.email!,
			parsedSurvey,
			$useCrypto,
			finalRing
		);

		const response = await fetch('/api/surveys/create', {
			method: 'POST',
			body: JSON.stringify(surveyInfo),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (!response.ok) {
			const body = await response.json();
			alert(body.detail);
			return;
		}

		const body = await response.json();
		ring = [];
		finalRing = [];
		surveyCode = body.survey_code;
		isSurveyModalHidden = false;
	}
</script>

{#if isPreview}
	<button title="Edit survey" class="footer-button" on:click={togglePreview}>
		<i class="material-symbols-rounded">edit</i>Edit
	</button>
{:else}
	<button
		title="Preview survey"
		class="footer-button"
		on:click={() => {
			$title.title = $title.title.trim();
			$questions = trimQuestions($questions);
			togglePreview();
		}}
	>
		<i class="material-symbols-rounded">search</i>Preview
	</button>
{/if}
<button
	title="Save draft"
	class="footer-button save popup"
	disabled={$questions.length === 0 || isPreview}
	on:click={saveDraft}
>
	<i class="material-symbols-rounded">save</i>Save Draft
	<span class="popup-text top" id="draft-popup">Saved!</span>
</button>
<button
	title="Finish survey creation"
	class="footer-button save done"
	disabled={$questions.length === 0 || isPreview}
	on:click={createSurvey}
>
	<i class="material-symbols-rounded">done</i>Create
</button>

<style>
	.popup {
		--tooltip-width: 4em;
	}

	.footer-button:disabled {
		color: var(--text-dark-color);
		background-color: var(--secondary-color);
		cursor: not-allowed;
	}

	.done i {
		font-variation-settings: 'wght' 700;
	}
</style>
