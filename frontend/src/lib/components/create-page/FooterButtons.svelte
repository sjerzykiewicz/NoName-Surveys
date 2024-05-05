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
	import SurveyInfo from '$lib/entities/SurveyCreateInfo';
	import { goto } from '$app/navigation';

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

	function processSurvey() {
		let parsedSurvey: Survey = new Survey($title, constructQuestionList());

		// TODO - replace dummy values with proper data
		let surveyInfo = new SurveyInfo(1, parsedSurvey, '31-12-9999', false);

		fetch('/api/surveys/create', {
			method: 'POST',
			body: JSON.stringify(surveyInfo),
			headers: {
				'Content-Type': 'application/json'
			}
		}).then((response) => {
			if (!response.ok) {
				// TODO - display what exactly is wrong
				alert(response.statusText);
			} else {
				response.json().then((data) => {
					const code = data.code;
					$title = '';
					$questions = [];
					goto(`/codeview/${code}`);
				});
			}
		});
	}
</script>

<button title="Preview survey" class="footer-button">
	<i class="material-symbols-rounded">search</i>Preview
</button>
<button title="Save survey" class="footer-button save" on:click={processSurvey}>
	<i class="material-symbols-rounded">save</i>Save
</button>

<style>
	@media screen and (max-width: 767px) {
		.footer-button {
			font-size: 1em;
		}
	}
</style>
