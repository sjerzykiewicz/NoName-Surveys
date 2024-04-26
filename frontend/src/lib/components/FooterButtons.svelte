<script lang="ts">
	import { title } from '$lib/stores';
	import { questions } from '$lib/stores';
	import * as Survey from '$lib/Survey';

	function parseSurvey() {
		let surveyTitle: string = $title;
		let questionList: Array<Survey.Question> = [];
		$questions.forEach((q) => {
			switch (q.component.name) {
				case 'Proxy<Single>':
					questionList = [
						...questionList,
						new Survey.SingleQuestion(q.required, q.question, q.choices)
					];
					break;
				case 'Proxy<Multi>':
					questionList = [
						...questionList,
						new Survey.MultiQuestion(q.required, q.question, q.choices)
					];
					break;
				case 'Proxy<Scale>':
					questionList = [...questionList, new Survey.ScaleQuestion(q.required, q.question)];
					break;
				case 'Proxy<Slider>':
					questionList = [
						...questionList,
						new Survey.SliderQuestion(
							q.required,
							q.question,
							parseFloat(q.choices[0]),
							parseFloat(q.choices[1])
						)
					];
					break;
				case 'Proxy<List>':
					questionList = [
						...questionList,
						new Survey.ListQuestion(q.required, q.question, q.choices)
					];
					break;
				case 'Proxy<Rank>':
					questionList = [
						...questionList,
						new Survey.RankQuestion(q.required, q.question, q.choices)
					];
					break;
				case 'Proxy<Text>':
					questionList = [
						...questionList,
						new Survey.TextQuestion(q.required, q.question, q.choices[0])
					];
			}
		});

		let parsedSurvey: Survey.Survey = new Survey.Survey(surveyTitle, questionList);

		// this will be removed later
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
		transition: background-color 0.3s;
		margin-left: 0.5em;
	}

	.footer-button:hover {
		background-color: #1a1a1a;
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
</style>
