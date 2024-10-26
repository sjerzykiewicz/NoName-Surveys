<script lang="ts">
	import { title, questions, answers } from '$lib/stores/fill-page';
	import Header from '$lib/components/Header.svelte';
	import Content from '$lib/components/Content.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import { TextQuestionAnswered, type TextQuestion } from '$lib/entities/questions/Text';
	import { SingleQuestion, SingleQuestionAnswered } from '$lib/entities/questions/Single';
	import { SliderQuestionAnswered, type SliderQuestion } from '$lib/entities/questions/Slider';
	import { NumberQuestionAnswered } from '$lib/entities/questions/Number';
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
	import Number from './Number.svelte';
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
	import { errorModalContent, isErrorModalHidden, M } from '$lib/stores/global';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import { FileError } from '$lib/entities/FileError';
	import KeysError from './KeysError.svelte';
	import { readFile } from '$lib/utils/readFile';

	onMount(async () => {
		await init();
	});

	export let survey: Survey;
	export let uses_crypto: boolean;
	export let keys: Array<string>;
	export let code: string;

	let innerWidth: number;
	let isSuccessModalHidden: boolean = true;
	let isKeysModalHidden: boolean = true;

	export const componentTypeMap: { [id: string]: ComponentType } = {
		text: Text,
		single: Single,
		multi: Multi,
		scale: Scale,
		binary: Binary,
		number: Number,
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
			case 'number':
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
						$answers[i].choices[0].trim()
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
					break;
				case 'number':
					answerList[i] = new NumberQuestionAnswered(
						$questions[i].required,
						$questions[i].question,
						parseFloat($questions[i].choices[0]),
						parseFloat($questions[i].choices[1]),
						parseFloat($answers[i].choices[0])
					);
					break;
			}
		}
		return answerList;
	}

	let unansweredRequired: Array<number> = [];

	async function checkAnswerCorrectness() {
		unansweredRequired = [];
		for (let i = 0; i < numQuestions; i++) {
			if ($questions[i].required) {
				if ($answers[i].choices.length === 0) {
					unansweredRequired.push(i);
				} else if (
					$answers[i].choices.some((c) => c === null || c === undefined || c.trim().length === 0)
				) {
					unansweredRequired.push(i);
				}
			}
		}

		if (unansweredRequired.length > 0) {
			await tick();
			scrollToElementById(unansweredRequired[0].toString());
			return false;
		}

		return true;
	}

	let fileElement: HTMLInputElement | null = null;
	let fileName: string = 'No file selected';
	let fileError: FileError = FileError.NoError;

	function handleFileChange() {
		fileElement = document.querySelector<HTMLInputElement>('#keys-file');
		fileName = fileElement?.files?.[0]?.name ?? 'No file selected';
	}

	function checkFileCorrectness() {
		fileError = FileError.NoError;

		if (fileElement?.files?.length === 0) {
			fileError = FileError.FileRequired;
			return false;
		} else if (fileElement?.files?.[0]?.name.split('.').pop() !== 'txt') {
			fileError = FileError.FileInvalid;
			return false;
		}

		return true;
	}

	async function processCrypto() {
		if (!checkFileCorrectness()) return;

		const text = await readFile(fileElement).then(
			(resolve) => {
				return resolve;
			},
			(reject) => {
				$errorModalContent = reject as string;
				$isErrorModalHidden = false;
				return '';
			}
		);

		let keyPair: KeyPair = getKeys(text);

		if (!keys.includes(keyPair.publicKey)) {
			$errorModalContent = 'Your public key is not on the list.';
			$isErrorModalHidden = false;
			return;
		}

		processForm(keyPair);
	}

	function getKeys(text: string): KeyPair {
		const words = text.split('\n');

		let publicKey = words[0];
		let privateKey = words[1];

		return new KeyPair(privateKey, publicKey);
	}

	async function processForm(keyPair: KeyPair | undefined) {
		let signature: string[] = [];

		const answerList: Array<Question> = constructAnswerList();

		if (uses_crypto) {
			const privateKey = keyPair!.privateKey;
			const publicKey = keyPair!.publicKey;
			const index = keys.indexOf(publicKey);

			try {
				signature = linkable_ring_signature(code, keys, privateKey, index);
			} catch (e) {
				$errorModalContent = e as string;
				$isErrorModalHidden = false;
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
			$errorModalContent = getErrorMessage(body.detail);
			$isErrorModalHidden = false;
			return;
		}

		isKeysModalHidden = true;
		isSuccessModalHidden = false;
	}

	async function submitSurvey() {
		if (!(await checkAnswerCorrectness())) return;
		if (uses_crypto) isKeysModalHidden = false;
		else processForm(undefined);
	}

	function hideSuccessModal() {
		isSuccessModalHidden = true;
		goto('/', { replaceState: true, invalidateAll: true });
	}

	onMount(() => {
		function handleSuccessEnter(event: KeyboardEvent) {
			if (!isSuccessModalHidden && event.key === 'Enter') {
				event.preventDefault();
				hideSuccessModal();
			}
		}

		function handleKeysEnter(event: KeyboardEvent) {
			if (!isKeysModalHidden && event.key === 'Enter') {
				event.preventDefault();
				processCrypto();
			}
		}

		document.body.addEventListener('keydown', handleSuccessEnter);
		document.body.addEventListener('keydown', handleKeysEnter);

		return () => {
			document.body.removeEventListener('keydown', handleSuccessEnter);
			document.body.removeEventListener('keydown', handleKeysEnter);
		};
	});
</script>

<svelte:window bind:innerWidth />

<Modal
	icon="encrypted"
	title="Load Your Keys"
	bind:isHidden={isKeysModalHidden}
	width={innerWidth <= $M ? 20 : 38}
>
	<div slot="content" title="Load your digital signature keys" class="file-div">
		<span class="file-label"
			>Please load the file which you have previously generated on this application. The file
			contains your keys, necessary for cryptographic calculations which are needed for validating
			your right to fill out this survey.<br /><br />Default filename: "noname-keys.txt"</span
		>
		<label for="keys-file">
			<div class="file-input">
				<span class="file-button"
					><i class="material-symbols-rounded">upload_file</i>Select File</span
				>
				<span class="file-name">{fileName}</span>
			</div>
			<input type="file" name="keys" id="keys-file" on:change={handleFileChange} />
		</label>
		<KeysError error={fileError} element={fileElement} />
	</div>
	<button title="Submit keys" class="save" on:click={processCrypto}
		><i class="material-symbols-rounded">done</i>Submit</button
	>
</Modal>

<Modal
	icon="check_circle"
	title="Survey Answered"
	bind:isHidden={isSuccessModalHidden}
	hide={hideSuccessModal}
>
	<span slot="content">Your answer has been submitted successfully.</span>
	<button title="Ok" class="save" on:click={hideSuccessModal}
		><i class="material-symbols-rounded">done</i>OK</button
	>
</Modal>

<Header>
	<div title="Survey title" class="title" in:slide={{ duration: 200, easing: cubicInOut }}>
		{$title}
	</div>
</Header>

<Content>
	{#if keys.length === 1 || keys.length === 2}
		<p title="Survey not secure" class="warning">
			<i class="material-symbols-rounded">warning</i>This survey is not secure.
			{keys.length === 1
				? ' You are the only person who can respond to this survey.'
				: ' There are only two people who can respond to this survey. The other person could be the creator of this survey.'}
		</p>
	{/if}
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
</Content>

<Footer>
	<button title="Submit survey" class="footer-button save" on:click={submitSurvey}>
		<i class="material-symbols-rounded">done</i>Submit
	</button>
</Footer>

<style>
	.file-div {
		width: 100%;
	}

	.save i {
		font-variation-settings: 'wght' 700;
	}

	.warning {
		margin: 0em 0em 0.5em 0em;
	}

	@media screen and (max-width: 768px) {
		.footer-button.save {
			font-size: 1.25em;
		}
	}
</style>
