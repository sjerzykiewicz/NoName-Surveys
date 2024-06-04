<script lang="ts">
	import { title, questions, answers } from '$lib/stores/fill-page';
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import { TextQuestionAnswered, type TextQuestion } from '$lib/entities/questions/Text';
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
	import QuestionTitle from './QuestionTitle.svelte';
	import Single from './Single.svelte';
	import Text from './Text.svelte';
	import List from './List.svelte';
	import Scale from './Scale.svelte';
	import Multi from './Multi.svelte';
	import Slider from './Slider.svelte';
	import Binary from './Binary.svelte';
	import Rank from './Rank.svelte';
	import type { ComponentType } from 'svelte';
	import AnswerError from './AnswerError.svelte';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { goto } from '$app/navigation';

	export let survey: Survey;
	export let uses_crypto: boolean;
	export let keys: Array<string>;

	export const componentTypeMap: { [id: string]: ComponentType } = {
		text: Text,
		single: Single,
		multi: Multi,
		scale: Scale,
		binary: Binary,
		slider: Slider,
		rank: Rank,
		list: List
	};

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

	function getPublicKeyFromFile(text: string): string {
		const words = text.split(' ');
		if (words.length > 1) {
			if (words[0] == 'ssh-rsa') {
				return words[1];
			}
		}
		return '';
	}

	function getPrivateKeyFromFile(text: string) {
		let lines = text.split('\n');
		lines.shift();
		lines.pop();
		const key = lines.join('');
		return key;
	}

	async function processForm() {
		const pubKeyInput = document.querySelector<HTMLInputElement>('#public-key');
		const keyInput = document.querySelector<HTMLInputElement>('#private-key');
		let publicKey: string = '';
		let privateKey: string = '';
		const publicReader = new FileReader();
		const publicFile = pubKeyInput?.files?.[0];
		const privateFile = keyInput?.files?.[0];
		if (publicFile) {
			publicReader.readAsText(publicFile);
			publicReader.onload = (e) => {
				const fileData = e.target?.result;
				const text = fileData as string;
				publicKey = getPublicKeyFromFile(text);
			};
		}

		const privateReader = new FileReader();
		if (privateFile) {
			privateReader.readAsText(privateFile);
			privateReader.onload = (e) => {
				const fileData = e.target?.result;
				const text = fileData as string;
				privateKey = getPrivateKeyFromFile(text);
			};
		}

		console.log(publicKey, privateKey);

		// unansweredRequired = [];
		// for (let i = 0; i < numQuestions; i++) {
		// 	if ($questions[i].required) {
		// 		if ($answers[i].choices.length === 0) {
		// 			unansweredRequired[i] = i;
		// 		} else if (
		// 			$answers[i].choices.some((c) => c === null || c === undefined || c.length === 0)
		// 		) {
		// 			unansweredRequired[i] = i;
		// 		}
		// 	}
		// }
		// if (unansweredRequired.length > 0) {
		// 	return;
		// }

		if (unansweredRequired.length > 0) {
			return;
		}

		const answerList: Array<Question> = constructAnswerList();
		const answer = new SurveyAnswer($page.params.code, answerList);

		if (!keys.includes(publicKey)) {
			alert('Provided public key is not on the list');
		} else {
			keys = keys.filter((key) => key !== publicKey);
			keys = [...keys, privateKey];
		}

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
			return await goto(`/`, { replaceState: true, invalidateAll: true });
		}
	}
</script>

<Header>
	<div title="Survey title" class="title" in:slide={{ duration: 200, easing: cubicInOut }}>
		{$title}
	</div>
</Header>

<Content>
	{#each $questions as question, questionIndex (question)}
		<div class="question" in:slide={{ duration: 200, easing: cubicInOut }}>
			<QuestionTitle {questionIndex} />
			<svelte:component this={componentTypeMap[question.type]} {questionIndex} />
		</div>
		<AnswerError {unansweredRequired} {questionIndex} />
	{/each}
	{#if uses_crypto}
		<label for="file">Choose public key file</label>
		<input type="file" name="public" id="public-key" />
		<label for="file">Choose private key file</label>
		<input type="file" name="private" id="private-key" />
	{/if}
</Content>

<Footer>
	<button title="Submit survey" class="footer-button save" on:click={processForm}>
		<i class="material-symbols-rounded">done</i>Submit
	</button>
</Footer>

<style>
	.save i {
		font-variation-settings: 'wght' 700;
	}
</style>
