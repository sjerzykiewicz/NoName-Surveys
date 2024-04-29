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
	import YesNoQuestion from '$lib/entities/questions/YesNo';
	import Survey from '$lib/entities/Survey';
	import Single from '$lib/components/create-page/Single.svelte';
	import Multi from '$lib/components/create-page/Multi.svelte';
	import Scale from '$lib/components/create-page/Scale.svelte';
	import Slider from '$lib/components/create-page/Slider.svelte';
	import List from '$lib/components/create-page/List.svelte';
	import Rank from '$lib/components/create-page/Rank.svelte';
	import Text from '$lib/components/create-page/Text.svelte';
	import YesNo from '$lib/components/create-page/YesNo.svelte';

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
				case YesNo:
					questionList = [...questionList, new YesNoQuestion(q.required, q.question)];
					break;
			}
		});

		return questionList;
	}

	function parseSurvey() {
		let parsedSurvey: Survey = new Survey($title, constructQuestionList());

		// TODO remove this later
		console.log(JSON.stringify(parsedSurvey));
	}
</script>

<a href="/create" title="Preview survey" class="footer-button">
	<i class="material-symbols-rounded">search</i>Preview
</a>
<button title="Save survey" class="footer-button save" on:click={parseSurvey}>
	<i class="material-symbols-rounded">save</i>Save
</button>

<style>
	.footer-button {
		display: flex;
		text-decoration: none;
		background-color: #4a4a4a;
		padding: 0.25em;
		border: 1px solid #999999;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		font-size: 1.25em;
		font-family: 'Jura';
		color: #eaeaea;
		cursor: pointer;
		transition: background-color 0.2s;
		margin-left: 0.5em;
	}

	.footer-button:hover {
		background-color: #1a1a1a;
	}

	.footer-button:active,
	.save:active {
		background-color: #999999;
	}

	.save {
		background-color: #0075ff;
	}

	.save:hover {
		background-color: #001c53;
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
