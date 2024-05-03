<script lang="ts">
	import { title } from '$lib/stores/create-page';
	import { questions } from '$lib/stores/create-page';
	import Question from '$lib/entities/questions/Question';
	import SingleQuestion from '$lib/entities/questions/Single';
	import MultiQuestion from '$lib/entities/questions/Multi';
	import ScaleQuestion from '$lib/entities/questions/Scale';
	import SliderQuestion from '$lib/entities/questions/Slider';
	import ListQuestion from '$lib/entities/questions/List';
	import RankQuestion from '$lib/entities/questions/Rank';
	import TextQuestion from '$lib/entities/questions/Text';
	import BinaryQuestion from '$lib/entities/questions/Binary';
	import Survey from '$lib/entities/Survey';
	import Single from '$lib/components/create-page/Single.svelte';
	import Multi from '$lib/components/create-page/Multi.svelte';
	import Scale from '$lib/components/create-page/Scale.svelte';
	import Slider from '$lib/components/create-page/Slider.svelte';
	import List from '$lib/components/create-page/List.svelte';
	import Rank from '$lib/components/create-page/Rank.svelte';
	import Text from '$lib/components/create-page/Text.svelte';
	import Binary from '$lib/components/create-page/Binary.svelte';

	function constructQuestionList() {
		let questionList: Array<Question> = [];
		$questions.forEach((q) => {
			switch (q.component) {
				case Single:
					questionList = [
						...questionList,
						new SingleQuestion(q.required, q.question, q.choices, undefined)
					];
					break;
				case Multi:
					questionList = [
						...questionList,
						new MultiQuestion(q.required, q.question, q.choices, undefined)
					];
					break;
				case Scale:
					questionList = [...questionList, new ScaleQuestion(q.required, q.question, undefined)];
					break;
				case Slider:
					questionList = [
						...questionList,
						new SliderQuestion(
							q.required,
							q.question,
							parseFloat(q.choices[0]),
							parseFloat(q.choices[1]),
							undefined
						)
					];
					break;
				case List:
					questionList = [
						...questionList,
						new ListQuestion(q.required, q.question, q.choices, undefined)
					];
					break;
				case Rank:
					questionList = [
						...questionList,
						new RankQuestion(q.required, q.question, q.choices, undefined)
					];
					break;
				case Text:
					questionList = [
						...questionList,
						new TextQuestion(q.required, q.question, q.choices[0], undefined)
					];
					break;
				case Binary:
					questionList = [
						...questionList,
						new BinaryQuestion(q.required, q.question, q.choices, undefined)
					];
					break;
			}
		});

		return questionList;
	}

	async function processSurvey() {
		let parsedSurvey: Survey = new Survey($title, constructQuestionList());

		let surveyDraft = {
			creator: 1, // TODO - replace with actual user ID
			title: $title,
			survey_structure: parsedSurvey
		};

		const response = await fetch('http://localhost:8000/survey-drafts/create', {
			method: 'POST',
			body: JSON.stringify(surveyDraft),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		// TODO - more precise info
		if (!response.ok) {
			alert('An error occured. Survey not saved.');
		}
	}
</script>

<a href="/create" title="Preview survey" class="footer-button">
	<i class="material-symbols-rounded">search</i>Preview
</a>
<button title="Save survey" class="footer-button save" on:click={processSurvey}>
	<i class="material-symbols-rounded">save</i>Save
</button>

<style>
	.footer-button {
		display: flex;
		text-decoration: none;
		background-color: var(--primary-color);
		padding: 0.25em;
		border: 1px solid var(--border-color);
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--box-shadow-color);
		font-size: 1.25em;
		font-family: 'Jura';
		color: #eaeaea;
		cursor: pointer;
		transition: background-color 0.2s;
		margin-left: 0.5em;
	}

	.footer-button:hover {
		background-color: var(--box-shadow-color);
	}

	.footer-button:active,
	.save:active {
		background-color: var(--border-color);
	}

	.save {
		background-color: var(--accent-color);
	}

	.save:hover {
		background-color: var(--accent-dark-color);
	}

	i {
		font-size: 1.15em;
		margin-right: 0.15em;
	}

	@media screen and (max-width: 767px) {
		.footer-button {
			font-size: 1em;
		}
	}
</style>
