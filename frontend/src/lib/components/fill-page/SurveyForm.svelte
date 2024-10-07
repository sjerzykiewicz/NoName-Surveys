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
	import { scrollToElementById } from '$lib/utils/scrollToElement';
	import { onMount, tick } from 'svelte';
	import init, { linkable_ring_signature } from 'wasm';
	import { getQuestionTypeData } from '$lib/utils/getQuestionTypeData';
	import Modal from '$lib/components/Modal.svelte';

	onMount(async () => {
		await init();
	});

	export let survey: Survey;
	export let uses_crypto: boolean;
	export let keys: Array<string>;
	export let code: string;

	let innerWidth: number;
	let isModalHidden: boolean = true;

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
			await tick();
			scrollToElementById(unansweredRequired[0].toString());
			return;
		}

		let signature: string[] = [];

		const answerList: Array<Question> = constructAnswerList();

		if (uses_crypto) {
			const privateKey = keyPair!.privateKey;
			const publicKey = keyPair!.publicKey;
			const index = keys.indexOf(publicKey);

			try {
				signature = linkable_ring_signature(code, keys, privateKey, index);
			} catch (e) {
				alert(e);
				return;
			}
		}

		const answer = new SurveyAnswer(code, answerList, signature);

		const response = await fetch('/api/surveys/fill', {
			method: 'POST',
			body: JSON.stringify(answer),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (!response.ok) {
			const body = await response.json();
			alert(body.detail);
		} else {
			isModalHidden = false;
		}
	}

	function getKeys(text: string): KeyPair {
		const words = text.split('\n');

		let publicKey = words[0];
		let privateKey = words[1];

		return new KeyPair(privateKey, publicKey);
	}

	function processCrypto() {
		const keyInput = document.querySelector<HTMLInputElement>('#keys-file');

		const keysReader = new FileReader();
		const keysFile = keyInput?.files?.[0];
		try {
			keysReader.readAsText(keysFile!);
		} catch {
			alert('No key file has been provided.');
			return;
		}
		let keyPair: KeyPair | undefined;
		keysReader.onload = (e) => {
			const fileData = e.target?.result;
			const text = fileData as string;
			keyPair = getKeys(text);
			if (!keys.includes(keyPair.publicKey)) {
				alert('Your public key is not on the list');
				return;
			}
			processForm(keyPair);
		};
	}

	function submitSurvey() {
		if (uses_crypto) {
			processCrypto();
		} else processForm(undefined);
	}

	let filename: string = 'No file chosen';

	function handleFileChange() {
		filename =
			document.querySelector<HTMLInputElement>('#keys-file')?.files?.[0]?.name ?? 'No file chosen';
	}

	function hideModal() {
		isModalHidden = true;
		goto('/', { replaceState: true, invalidateAll: true });
	}

	const TOOLTIP_BREAKPOINT = 615;
</script>

<svelte:window bind:innerWidth />

<Modal icon="check_circle" title="Survey Answered" bind:isHidden={isModalHidden} hide={hideModal}>
	<span slot="content">Your answer has been submitted successfully.</span>
	<button title="Ok" class="save" on:click={hideModal}
		><i class="material-symbols-rounded">done</i>OK</button
	>
</Modal>

<Header>
	<div title="Survey title" class="title" in:slide={{ duration: 200, easing: cubicInOut }}>
		{$title}
	</div>
</Header>

<Content>
	{#each $questions as question, questionIndex (question)}
		<div class="question" in:slide={{ duration: 200, easing: cubicInOut }}>
			<QuestionTitle
				{questionIndex}
				questionTypeData={getQuestionTypeData(componentTypeMap[question.type])}
			/>
			<svelte:component this={componentTypeMap[question.type]} {questionIndex} />
		</div>
		<AnswerError {unansweredRequired} {questionIndex} />
	{/each}
	{#if uses_crypto}
		<div title="Load your digital signature keys" class="load-div">
			<div class="load-text">
				<span class="load-label">Load your keys</span>
				<div title="" class="tooltip">
					<i class="material-symbols-rounded">info</i>
					<span class="tooltip-text {innerWidth <= TOOLTIP_BREAKPOINT ? 'top' : 'right'}"
						>Please load the file which you have previously generated on this application. The file
						contains your keys, necessary for cryptographic calculations which are needed for
						validating your right to fill out this survey.<br /><br />Default filename:
						"noname-keys.txt"</span
					>
				</div>
			</div>
			<label for="keys-file">
				<div class="file-input">
					<span class="file-button"
						><i class="material-symbols-rounded">upload_file</i>Choose File</span
					>
					<span class="file-name">{filename}</span>
				</div>
				<input type="file" name="keys" id="keys-file" on:change={handleFileChange} />
			</label>
		</div>
	{/if}
</Content>

<Footer>
	<button title="Submit survey" class="footer-button save" on:click={submitSurvey}>
		<i class="material-symbols-rounded">done</i>Submit
	</button>
</Footer>

<style>
	.tooltip {
		--tooltip-width: 38em;
		margin-left: 0.5em;
	}

	.tooltip i {
		font-size: 1em;
	}

	.load-div {
		color: var(--text-color);
		font-size: 1.25em;
		text-shadow: 0px 4px 4px var(--shadow-color);
		width: 100%;
		text-align: center;
		margin-top: 2.25em;
		padding-top: 1.5em;
		border-top: 1px solid var(--border-color);
	}

	.load-text {
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: flex-start;
	}

	.load-label {
		cursor: default;
	}

	.load-text,
	.load-div label {
		font-size: 1.2em;
	}

	input[type='file'] {
		display: none;
	}

	.file-input {
		display: flex;
		flex-direction: row;
		justify-content: flex-start;
		align-items: center;
		text-align: left;
		width: fit-content;
		margin-top: 0.5em;
		background-color: var(--secondary-dark-color);
		border: 1px solid var(--border-color);
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--shadow-color);
		padding: 0.5em;
		font-size: 0.8em;
		cursor: default;
	}

	.file-button {
		display: flex;
		align-items: center;
		padding: 0.25em;
		background-color: var(--primary-color);
		border: 1px solid var(--border-color);
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--shadow-color);
		text-shadow: none;
		color: var(--text-color);
		cursor: pointer;
		transition: 0.2s;
		margin-right: 0.5em;
		min-width: 7em;
	}

	.file-button:hover {
		background-color: var(--secondary-color);
	}

	.file-button:active {
		background-color: var(--border-color);
	}

	.file-name {
		overflow: hidden;
		overflow-wrap: anywhere;
		text-overflow: ellipsis;
		height: 1.15em;
	}

	.save i {
		font-variation-settings: 'wght' 700;
	}

	@media screen and (max-width: 1193px) {
		.tooltip {
			--tooltip-width: 26.9em;
		}
	}

	@media screen and (max-width: 767px) {
		.load-div {
			font-size: 1em;
		}

		.save {
			font-size: 1.25em;
		}

		.file-input {
			flex-flow: column;
		}

		.file-button {
			margin-right: 0em;
			margin-bottom: 0.5em;
		}
	}

	@media screen and (max-width: 615px) {
		.tooltip {
			--tooltip-width: 17em;
		}
	}
</style>
