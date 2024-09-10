<script lang="ts">
	import {
		title,
		questions,
		previousQuestion,
		isAccessLimited,
		ringMembers
	} from '$lib/stores/create-page';
	import Question from '$lib/entities/questions/Question';
	import { SingleQuestion } from '$lib/entities/questions/Single';
	import { MultiQuestion } from '$lib/entities/questions/Multi';
	import { ScaleQuestion } from '$lib/entities/questions/Scale';
	import { SliderQuestion } from '$lib/entities/questions/Slider';
	import { ListQuestion } from '$lib/entities/questions/List';
	import { RankQuestion } from '$lib/entities/questions/Rank';
	import { TextQuestion } from '$lib/entities/questions/Text';
	import { BinaryQuestion } from '$lib/entities/questions/Binary';
	import Survey from '$lib/entities/surveys/Survey';
	import Single from '$lib/components/create-page/Single.svelte';
	import Multi from '$lib/components/create-page/Multi.svelte';
	import Scale from '$lib/components/create-page/Scale.svelte';
	import Slider from '$lib/components/create-page/Slider.svelte';
	import List from '$lib/components/create-page/List.svelte';
	import Rank from '$lib/components/create-page/Rank.svelte';
	import Text from '$lib/components/create-page/Text.svelte';
	import Binary from '$lib/components/create-page/Binary.svelte';
	import SurveyInfo from '$lib/entities/surveys/SurveyCreateInfo';
	import { goto } from '$app/navigation';
	import { QuestionError } from '$lib/entities/QuestionError';
	import { scrollToElementById } from '$lib/utils/scrollToElement';
	import { delay } from '$lib/utils/delay';
	import DraftCreateInfo from '$lib/entities/surveys/DraftCreateInfo';
	import { tick } from 'svelte';
	import { page } from '$app/stores';
	import { error } from '@sveltejs/kit';
	import { fade } from 'svelte/transition';
	import { cubicInOut } from 'svelte/easing';

	export let isPreview: boolean = false;

	function togglePreview() {
		isPreview = !isPreview;
	}

	function constructQuestionList() {
		let questionList: Array<Question> = [];
		$questions.forEach((q) => {
			switch (q.component) {
				case Single:
					questionList = [...questionList, new SingleQuestion(q.required, q.question, q.choices)];
					break;
				case Multi:
					questionList = [...questionList, new MultiQuestion(q.required, q.question, q.choices)];
					break;
				case Scale:
					questionList = [...questionList, new ScaleQuestion(q.required, q.question)];
					break;
				case Slider:
					questionList = [
						...questionList,
						new SliderQuestion(
							q.required,
							q.question,
							parseFloat(q.choices[0]),
							parseFloat(q.choices[1])
						)
					];
					break;
				case List:
					questionList = [...questionList, new ListQuestion(q.required, q.question, q.choices)];
					break;
				case Rank:
					questionList = [...questionList, new RankQuestion(q.required, q.question, q.choices)];
					break;
				case Text:
					questionList = [...questionList, new TextQuestion(q.required, q.question, q.choices[0])];
					break;
				case Binary:
					questionList = [...questionList, new BinaryQuestion(q.required, q.question, q.choices)];
					break;
			}
		});

		return questionList;
	}

	export let titleError: boolean = false;

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

		return true;
	}

	let isDraftPopupVisible: boolean = false;

	async function saveDraft() {
		if (!(await checkCorrectness())) return;
		const parsedSurvey = new Survey($title, constructQuestionList());
		const draftInfo = new DraftCreateInfo($page.data.session!.user!.email!, parsedSurvey);

		const response = await fetch('/api/surveys/drafts/create', {
			method: 'POST',
			body: JSON.stringify(draftInfo),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (!response.ok) {
			error(response.status, { message: await response.json() });
		} else {
			isDraftPopupVisible = true;
			await delay(2000);
			isDraftPopupVisible = false;
		}
	}

	async function createSurvey() {
		if (!(await checkCorrectness())) return;
		const parsedSurvey = new Survey($title, constructQuestionList());

		const useCrypto = $ringMembers.length !== 0;
		const surveyInfo = new SurveyInfo(
			$page.data.session!.user!.email!,
			parsedSurvey,
			useCrypto,
			$ringMembers
		);

		const response = await fetch('/api/surveys/create', {
			method: 'POST',
			body: JSON.stringify(surveyInfo),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (!response.ok) {
			error(response.status, { message: await response.json() });
		} else {
			const body = await response.json();
			$title = '';
			$questions = [];
			$previousQuestion = null;
			$isAccessLimited = false;
			$ringMembers = [];
			return await goto(`/${body.survey_code}/view`, { replaceState: true, invalidateAll: true });
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
	{#if isDraftPopupVisible}
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
