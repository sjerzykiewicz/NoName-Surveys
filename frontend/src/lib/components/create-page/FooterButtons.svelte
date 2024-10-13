<script lang="ts">
	import {
		title,
		questions,
		previousQuestion,
		useCrypto,
		ringMembers,
		selectedGroup,
		isDraftModalHidden,
		isDraftPopupVisible,
		currentDraftId,
		draft
	} from '$lib/stores/create-page';
	import Survey from '$lib/entities/surveys/Survey';
	import Slider from '$lib/components/create-page/Slider.svelte';
	import Text from '$lib/components/create-page/Text.svelte';
	import Binary from '$lib/components/create-page/Binary.svelte';
	import SurveyInfo from '$lib/entities/surveys/SurveyCreateInfo';
	import { goto } from '$app/navigation';
	import { SurveyError } from '$lib/entities/SurveyError';
	import { scrollToElementById } from '$lib/utils/scrollToElement';
	import { tick } from 'svelte';
	import { page } from '$app/stores';
	import { error } from '@sveltejs/kit';
	import { fade } from 'svelte/transition';
	import { cubicInOut } from 'svelte/easing';
	import { constructQuestionList } from '$lib/utils/constructQuestionList';
	import { delay } from '$lib/utils/delay';
	import DraftCreateInfo from '$lib/entities/surveys/DraftCreateInfo';
	import { getDraft } from '$lib/utils/getDraft';
	import { trimQuestions } from '$lib/utils/trimQuestions';
	import { LIMIT_OF_CHARS } from '$lib/stores/global';

	export let isPreview: boolean = false;
	export let cryptoError: boolean = false;

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
				$questions[i].component === Slider &&
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
			$isDraftModalHidden = false;
		} else {
			const parsedSurvey = new Survey($title.title, constructQuestionList($questions));
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
				$draft = getDraft($title.title, $questions);
				$isDraftPopupVisible = true;
				await delay(2000);
				$isDraftPopupVisible = false;
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
		} else {
			const body = await response.json();
			$title = { title: '', error: SurveyError.NoError };
			$questions = [];
			$previousQuestion = null;
			$useCrypto = false;
			$ringMembers = [];
			$selectedGroup = [];
			$currentDraftId = null;
			$draft = getDraft('', []);
			ring = [];
			finalRing = [];
			return await goto(`/${body.survey_code}/view`, { replaceState: true, invalidateAll: true });
		}
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
	disabled={$questions.length === 0 || isPreview || $isDraftPopupVisible}
	on:click={saveDraft}
>
	<i class="material-symbols-rounded">save</i>Save Draft
	{#if $isDraftPopupVisible}
		<span class="popup-text top" transition:fade={{ duration: 200, easing: cubicInOut }}
			>Saved!</span
		>
	{/if}
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
