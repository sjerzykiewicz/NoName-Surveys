<script lang="ts">
	import { title } from '$lib/stores/create-page';
	import { questions } from '$lib/stores/create-page';
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
	import { scrollToElement } from '$lib/utils/scrollToElement';
	import DraftCreateInfo from '$lib/entities/surveys/DraftCreateInfo';
	import { tick } from 'svelte';

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

		if (!$title) {
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

		if (!$questions.every((q) => q.error === QuestionError.NoError) || titleError) {
			await tick();
			scrollToElement('.error');
			return false;
		}

		return true;
	}

	async function saveDraft() {
		if (!(await checkCorrectness())) return;
		const parsedSurvey = new Survey($title, constructQuestionList());
		// TODO - user id
		const draftInfo = new DraftCreateInfo(1, parsedSurvey);

		const response = await fetch('/api/surveys/drafts/create', {
			method: 'POST',
			body: JSON.stringify(draftInfo),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (!response.ok) {
			alert(response.statusText);
		} else {
			// TODO - display in UI
			alert('Saved');
		}
	}

	async function createSurvey() {
		if (!(await checkCorrectness())) return;
		const parsedSurvey = new Survey($title, constructQuestionList());

		// TODO - replace dummy values with proper data
		const surveyInfo = new SurveyInfo(1, parsedSurvey, '31-12-9999', false);

		const response = await fetch('/api/surveys/create', {
			method: 'POST',
			body: JSON.stringify(surveyInfo),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (!response.ok) {
			// TODO - display what exactly is wrong
			alert(response.statusText);
		} else {
			const code = (await response.json()).code;
			$title = '';
			$questions = [];
			return await goto(`/${code}/view`, { replaceState: true, invalidateAll: true });
		}
	}
</script>

<button title="Preview survey" class="footer-button">
	<i class="material-symbols-rounded">search</i>Preview
</button>
<button
	title="Save draft"
	class="footer-button save"
	disabled={$questions.length === 0}
	on:click={saveDraft}
>
	<i class="material-symbols-rounded">save</i>Save draft
</button>
<button
	title="Finish"
	class="footer-button save"
	disabled={$questions.length === 0}
	on:click={createSurvey}
>
	<i class="material-symbols-rounded">done</i>Finish
</button>

<style>
	.save:disabled {
		color: var(--text-dark-color);
		background-color: var(--secondary-color);
		cursor: not-allowed;
	}

	@media screen and (max-width: 767px) {
		.footer-button {
			font-size: 1em;
		}
	}
</style>
