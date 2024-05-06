<script lang="ts">
	import { answers, questions } from '$lib/stores/fill-page';
	import type { ComponentType } from 'svelte';
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import SurveyTitle from '$lib/components/fill-page/SurveyTitle.svelte';
	import Single from '$lib/components/fill-page/Single.svelte';
	import Text from '$lib/components/fill-page/Text.svelte';
	import List from '$lib/components/fill-page/List.svelte';
	import Scale from '$lib/components/fill-page/Scale.svelte';
	import QuestionTitle from '$lib/components/fill-page/QuestionTitle.svelte';
	import Multi from '$lib/components/fill-page/Multi.svelte';
	import Slider from '$lib/components/fill-page/Slider.svelte';
	import Binary from '$lib/components/fill-page/Binary.svelte';
	import Rank from '$lib/components/fill-page/Rank.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import { TextQuestionAnswered, type TextQuestion } from '$lib/entities/questions/Text';
	import { title } from '$lib/stores/fill-page';
	import { SingleQuestion, SingleQuestionAnswered } from '$lib/entities/questions/Single';
	import { SliderQuestionAnswered, type SliderQuestion } from '$lib/entities/questions/Slider';
	import type Survey from '$lib/entities/surveys/Survey';
	import type Question from '$lib/entities/questions/Question';
	import { MultiQuestionAnswered } from '$lib/entities/questions/Multi';
	import { BinaryQuestionAnswered } from '$lib/entities/questions/Binary';
	import { RankQuestionAnswered } from '$lib/entities/questions/Rank';
	import { ListQuestionAnswered } from '$lib/entities/questions/List';
	import { ScaleQuestionAnswered } from '$lib/entities/questions/Scale';
	import { SurveyAnswer } from '$lib/entities/surveys/SurveyAnswer';
	import { page } from '$app/stores';
	import { goto } from '$app/navigation';

	const componentTypeMap: { [id: string]: ComponentType } = {
		text: Text,
		single: Single,
		multi: Multi,
		scale: Scale,
		binary: Binary,
		slider: Slider,
		rank: Rank,
		list: List
	};

	export let survey: Survey;

	$title = survey.title;

	for (let i in survey.questions) {
		$questions[i] = {
			type: survey.questions[i].question_type,
			required: survey.questions[i].required,
			question: survey.questions[i].question,
			choices: []
		};
		switch (survey.questions[i].question_type) {
			case 'text':
				$questions[i].choices[0] = (survey.questions[i] as TextQuestion).details;
				break;
			case 'scale':
				$questions[i].choices = ['1', '2', '3', '4', '5'];
				break;
			case 'slider':
				$questions[i].choices[0] = (survey.questions[i] as SliderQuestion).min_value.toString();
				$questions[i].choices[1] = (survey.questions[i] as SliderQuestion).max_value.toString();
				break;
			default:
				$questions[i].choices = (survey.questions[i] as SingleQuestion).choices;
				break;
		}
	}

	const numQuestions = $questions.length;
	for (let i = 0; i < numQuestions; i++) {
		$answers = [...$answers, { choices: [] }];
	}

	function constructAnswerList() {
		let answerList: Array<Question> = [];
		for (let i = 0; i < numQuestions; i++) {
			const type = $questions[i].type;
			switch (type) {
				case 'single':
					answerList[i] = new SingleQuestionAnswered(
						$questions[i].required,
						$questions[i].question,
						$questions[i].choices,
						$answers[i].choices[0]
					);
					break;
				case 'multi':
					answerList[i] = new MultiQuestionAnswered(
						$questions[i].required,
						$questions[i].question,
						$questions[i].choices,
						$answers[i].choices
					);
					break;
				case 'binary':
					answerList[i] = new BinaryQuestionAnswered(
						$questions[i].required,
						$questions[i].question,
						$questions[i].choices,
						$answers[i].choices[0]
					);
					break;
				case 'rank':
					answerList[i] = new RankQuestionAnswered(
						$questions[i].required,
						$questions[i].question,
						$questions[i].choices,
						$answers[i].choices
					);
					break;
				case 'list':
					answerList[i] = new ListQuestionAnswered(
						$questions[i].required,
						$questions[i].question,
						$questions[i].choices,
						$answers[i].choices[0]
					);
					break;
				case 'scale':
					answerList[i] = new ScaleQuestionAnswered(
						$questions[i].required,
						$questions[i].question,
						parseFloat($answers[i].choices[0])
					);
					break;
				case 'text':
					answerList[i] = new TextQuestionAnswered(
						$questions[i].required,
						$questions[i].question,
						$questions[i].choices[0],
						$answers[i].choices[0]
					);
					break;
				case 'slider':
					answerList[i] = new SliderQuestionAnswered(
						$questions[i].required,
						$questions[i].question,
						parseFloat($questions[i].choices[0]),
						parseFloat($questions[i].choices[1]),
						parseFloat($answers[i].choices[0])
					);
			}
		}
		return answerList;
	}

	let unansweredRequired: Array<number> = [];

	async function processForm() {
		unansweredRequired = [];
		for (let i = 0; i < numQuestions; i++) {
			// TODO - remove console log
			console.log($answers[i].choices);
			if ($questions[i].required) {
				if ($answers[i].choices.length === 0) {
					unansweredRequired[i] = i;
				} else {
					for (let j in $answers[i].choices) {
						let choice = $answers[i].choices[j];
						if (choice === null || choice === undefined || choice.length === 0) {
							unansweredRequired[i] = i;
						}
					}
				}
			}
		}
		if (unansweredRequired.length > 0) {
			return;
		}
		const answerList: Array<Question> = constructAnswerList();
		const answer = new SurveyAnswer($page.params.code, answerList);

		const response = await fetch('/api/surveys/fill', {
			method: 'POST',
			body: JSON.stringify(answer),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (!response.ok) {
			// TODO - display what exactly is wrong
			alert(response.statusText);
		} else {
			return await goto(`/welcome`, { replaceState: true, invalidateAll: true });
		}
	}
</script>

<Header>
	<SurveyTitle />
</Header>
<Content>
	{#each $questions as question, questionIndex}
		<div class="question">
			<QuestionTitle {questionIndex} />
			<svelte:component this={componentTypeMap[question.type]} {questionIndex} />
		</div>
		{#if unansweredRequired.includes(questionIndex)}
			<p class="error">*An answer to question {questionIndex + 1} is required!</p>
		{/if}
	{/each}
</Content>
<Footer>
	<button title="Submit survey" class="footer-button submit" on:click={processForm}>
		<i class="material-symbols-rounded">done</i>Submit
	</button>
</Footer>

<style>
	.question {
		margin-bottom: 1.875em;
	}

	.error {
		padding-left: 2.3em;
	}

	@media screen and (max-width: 767px) {
		.footer-button {
			font-size: 1em;
		}
	}
</style>
