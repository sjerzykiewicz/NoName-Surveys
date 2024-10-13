<script lang="ts">
	import {
		title,
		questions,
		useCrypto,
		ringMembers,
		selectedGroup,
		currentDraftId,
		draft
	} from '$lib/stores/create-page';
	import Survey from '$lib/entities/surveys/Survey';
	import Slider from '$lib/components/create-page/Slider.svelte';
	import Text from '$lib/components/create-page/Text.svelte';
	import Binary from '$lib/components/create-page/Binary.svelte';
	import SurveyInfo from '$lib/entities/surveys/SurveyCreateInfo';
	import { QuestionError } from '$lib/entities/QuestionError';
	import { scrollToElementById } from '$lib/utils/scrollToElement';
	import { tick } from 'svelte';
	import { page } from '$app/stores';
	import { error } from '@sveltejs/kit';
	import { constructQuestionList } from '$lib/utils/constructQuestionList';
	import { popup } from '$lib/utils/popup';
	import DraftCreateInfo from '$lib/entities/surveys/DraftCreateInfo';
	import { getDraft } from '$lib/utils/getDraft';

	export let isPreview: boolean = false;
	export let titleError: boolean = false;
	export let cryptoError: boolean = false;
	export let isDraftModalHidden: boolean = true;
	export let isSurveyModalHidden: boolean = true;
	export let surveyCode: string;

	function togglePreview() {
		isPreview = !isPreview;
	}

	async function checkCorrectness() {
		titleError = false;
		const t = $title;
		if (t === null || t === undefined || t.length === 0) {
			titleError = true;
		}

		const numQuestions = $questions.length;

		for (let i = 0; i < numQuestions; i++) {
			const q = $questions[i].question;
			if (q === null || q === undefined || q.length === 0) {
				$questions[i].error = QuestionError.QuestionRequired;
			} else if (
				$questions[i].component != Text &&
				$questions[i].choices.some((c) => c === null || c === undefined || c.length === 0)
			) {
				switch ($questions[i].component) {
					case Slider:
						$questions[i].error = QuestionError.SliderValuesRequired;
						break;
					case Binary:
						$questions[i].error = QuestionError.BinaryChoicesRequired;
						break;
					default:
						$questions[i].error = QuestionError.ChoicesRequired;
				}
			} else if (
				$questions[i].component === Slider &&
				parseFloat($questions[i].choices[0]) >= parseFloat($questions[i].choices[1])
			) {
				$questions[i].error = QuestionError.ImproperSliderValues;
			} else if (new Set($questions[i].choices).size !== $questions[i].choices.length) {
				$questions[i].error = QuestionError.DuplicateChoices;
			} else {
				$questions[i].error = QuestionError.NoError;
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

		if (titleError) {
			await tick();
			scrollToElementById('header');
			return false;
		}

		if (!$questions.every((q) => q.error === QuestionError.NoError)) {
			await tick();
			scrollToElementById(
				$questions.indexOf($questions.find((q) => q.error !== QuestionError.NoError)!).toString()
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
		if (!(await checkCorrectness())) return;
		if ($currentDraftId !== null) {
			isDraftModalHidden = false;
		} else {
			const parsedSurvey = new Survey($title, constructQuestionList($questions));
			const draftInfo = new DraftCreateInfo($page.data.session!.user!.email!, parsedSurvey);

			const createResponse = await fetch('/api/surveys/drafts/create', {
				method: 'POST',
				body: JSON.stringify(draftInfo),
				headers: {
					'Content-Type': 'application/json'
				}
			});

			if (!createResponse.ok) {
				error(createResponse.status, { message: await createResponse.json() });
			} else {
				$currentDraftId = await createResponse.json();
				$draft = getDraft($title, $questions);
				popup('draft-popup');
			}
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
		} else {
			const body = await response.json();
			ring = [...$ringMembers, ...body];
		}
	}

	async function createSurvey() {
		if (!(await checkCorrectness())) return;

		const parsedSurvey = new Survey($title, constructQuestionList($questions));
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
		} else {
			const body = await response.json();
			ring = [];
			finalRing = [];
			surveyCode = body.survey_code;
			isSurveyModalHidden = false;
		}
	}
</script>

{#if isPreview}
	<button title="Edit survey" class="footer-button" on:click={togglePreview}>
		<i class="material-symbols-rounded">edit</i>Edit
	</button>
{:else}
	<button title="Preview survey" class="footer-button" on:click={togglePreview}>
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
