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
	import KeyPair from '$lib/entities/KeyPair';

	// import { onMount } from 'svelte';
	// import init, { Ring } from 'wasm';

	// onMount(async () => {
	// 	await init();
	// });

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

	async function processForm(keyPair: KeyPair | undefined) {
		unansweredRequired = [];
		for (let i = 0; i < numQuestions; i++) {
			if ($questions[i].required) {
				if ($answers[i].choices.length === 0) {
					unansweredRequired[i] = i;
				} else if (
					$answers[i].choices.some((c) => c === null || c === undefined || c.length === 0)
				) {
					unansweredRequired[i] = i;
				}
			}
		}
		if (unansweredRequired.length > 0) {
			return;
		}

		if (unansweredRequired.length > 0) {
			return;
		}

		let signature = [123];
		let y0 = '1234';

		const answerList: Array<Question> = constructAnswerList();

		if (uses_crypto) {
			// const privateKey = keyPair!.privateKey;
			// const index = keys.indexOf(keyPair!.publicKey);
			keys = keys.filter((k) => k !== keyPair!.publicKey);
		}

		const answer = new SurveyAnswer($page.params.code, answerList, signature, y0);

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

	function getKeys(text: string): KeyPair {
		const words = text.split('\n\n');

		let publicKey = words[0] + '\n';
		let privateKey = words[1];

		return new KeyPair(privateKey, publicKey);
	}

	function processCrypto() {
		const keyInput = document.querySelector<HTMLInputElement>('#keys-file');

		const keysReader = new FileReader();
		const keysFile = keyInput?.files?.[0];
		keysReader.readAsText(keysFile!);
		let keyPair: KeyPair | undefined;
		keysReader.onload = (e) => {
			const fileData = e.target?.result;
			const text = fileData as string;
			keyPair = getKeys(text);
			if (!keys.includes(keyPair.publicKey)) {
				alert('Your public key is not on the list');
			}
			processForm(keyPair);
		};
	}

	async function submitSurvey() {
		if (uses_crypto) {
			processCrypto();
		} else processForm(undefined);
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
		<label for="file">Upload your keys</label>
		<input type="file" name="keys" id="keys-file" />
	{/if}
</Content>

<Footer>
	<button title="Submit survey" class="footer-button save" on:click={submitSurvey}>
		<i class="material-symbols-rounded">done</i>Submit
	</button>
</Footer>

<style>
	input[type='file'] {
		margin-top: 0.5em;
		background-color: var(--secondary-dark-color);
		border: 1px solid var(--border-color);
		border-radius: 5px;
		font-size: 0.8em;
		cursor: default;
	}

	input[type='file']::file-selector-button {
		padding: 0.25em;
		background-color: var(--primary-color);
		border: none;
		border-right: 1px solid var(--border-color);
		color: var(--text-color);
		font-family: 'Jura';
		cursor: pointer;
		transition: 0.2s;
	}

	input[type='file']::file-selector-button:hover {
		background-color: var(--secondary-color);
	}

	input[type='file']::file-selector-button:active {
		background-color: var(--border-color);
	}

	.save {
		margin-top: 0.5em;
		font-size: 1em;
	}

	.save i {
		font-variation-settings: 'wght' 700;
	}
</style>
