<script lang="ts">
	import { title, questions, answers } from '$lib/stores/fill-page';
	import Header from '$lib/components/global/Header.svelte';
	import Content from '$lib/components/global/Content.svelte';
	import Footer from '$lib/components/global/Footer.svelte';
	import { TextQuestionAnswered, type TextQuestion } from '$lib/entities/questions/Text';
	import { SingleQuestion, SingleQuestionAnswered } from '$lib/entities/questions/Single';
	import { SliderQuestionAnswered, type SliderQuestion } from '$lib/entities/questions/Slider';
	import { NumberQuestion, NumberQuestionAnswered } from '$lib/entities/questions/Number';
	import type Survey from '$lib/entities/surveys/Survey';
	import type Question from '$lib/entities/questions/Question';
	import { MultiQuestionAnswered } from '$lib/entities/questions/Multi';
	import { BinaryQuestionAnswered } from '$lib/entities/questions/Binary';
	import { RankQuestionAnswered } from '$lib/entities/questions/Rank';
	import { ListQuestionAnswered } from '$lib/entities/questions/List';
	import { ScaleQuestionAnswered } from '$lib/entities/questions/Scale';
	import SurveyAnswer from '$lib/entities/surveys/SurveyAnswer';
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
	import Modal from '$lib/components/global/Modal.svelte';
	import {
		errorModalContent,
		isErrorModalHidden,
		successModalContent,
		isSuccessModalHidden,
		M
	} from '$lib/stores/global';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import { FileError } from '$lib/entities/FileError';
	import KeysError from './KeysError.svelte';
	import { readFile } from '$lib/utils/readFile';
	import SuccessModal from '$lib/components/global/SuccessModal.svelte';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	onMount(async () => {
		await init();
	});

	export let survey_title: string;
	export let survey: Survey;
	export let code: string;
	export let uses_crypto: boolean;
	export let keys: Array<string>;

	let innerWidth: number;
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

	$title = survey_title;

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
				$questions[i].choices[2] = (survey.questions[i] as SliderQuestion).precision.toString();
				break;
			case 'number':
				$questions[i].choices[0] = (survey.questions[i] as NumberQuestion).min_value.toString();
				$questions[i].choices[1] = (survey.questions[i] as NumberQuestion).max_value.toString();
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
						parseFloat($questions[i].choices[2]),
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

	let unansweredRequired: Set<number> = new Set();

	async function checkAnswerCorrectness() {
		unansweredRequired = new Set();
		for (let i = 0; i < numQuestions; i++) {
			if ($questions[i].required) {
				if ($answers[i].choices.length === 0) {
					unansweredRequired.add(i);
				} else if (
					$answers[i].choices.some((c) => c === null || c === undefined || c.trim().length === 0)
				) {
					unansweredRequired.add(i);
				}
			}
		}

		if (unansweredRequired.size > 0) {
			await tick();
			const [first] = unansweredRequired;
			scrollToElementById(first.toString());
			return false;
		}

		return true;
	}

	let fileElement: HTMLInputElement | null = null;
	let fileName: string = $t('no_file_selected');
	let fileError: FileError = FileError.NoError;

	function handleFileChange() {
		fileName = fileElement?.files?.[0]?.name ?? $t('no_file_selected');
	}

	function checkFileCorrectness() {
		fileError = FileError.NoError;

		if (fileElement?.files?.length === 0) {
			fileError = FileError.FileRequired;
			return false;
		} else if (fileElement?.files?.[0]?.name.split('.').pop() !== 'pem') {
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
			$errorModalContent = $t('public_key_not_on_list');
			$isErrorModalHidden = false;
			return;
		}

		processForm(keyPair);
	}

	function getKeys(text: string): KeyPair {
		const words = text.split('\n\n');

		let publicKey = words[0] + '\n';
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
		$successModalContent = $t('answer_submit_success');
		$isSuccessModalHidden = false;
	}

	async function submitSurvey() {
		if (!(await checkAnswerCorrectness())) return;
		if (uses_crypto) isKeysModalHidden = false;
		else processForm(undefined);
	}

	async function hideSuccessModal() {
		$isSuccessModalHidden = true;
		await goto('/', { replaceState: true, invalidateAll: true });
	}

	onMount(() => {
		function handleEnter(event: KeyboardEvent) {
			if (!isKeysModalHidden && event.key === 'Enter') {
				event.preventDefault();
				processCrypto();
				event.stopImmediatePropagation();
			}
		}

		document.body.addEventListener('keydown', handleEnter);

		return () => {
			document.body.removeEventListener('keydown', handleEnter);
		};
	});
</script>

<svelte:window bind:innerWidth />

<SuccessModal hide={hideSuccessModal} />

<Modal
	icon="encrypted"
	title={$t('load_keys_title')}
	bind:isHidden={isKeysModalHidden}
	--width={innerWidth <= $M ? '20em' : '38em'}
>
	<div slot="content" title={$t('load_keys')} class="file-div">
		<span class="file-label"
			><Tx text="key_file_label" /><br /><br /><Tx text="default_filename" />: "noname-keys.pem"</span
		>
		<label>
			<div class="file-input">
				<span class="file-button"><i class="symbol">upload_file</i><Tx text="select_file" /></span>
				<span class="file-name">{fileName}</span>
			</div>
			<input type="file" bind:this={fileElement} on:change={handleFileChange} />
		</label>
		<KeysError error={fileError} element={fileElement} />
	</div>
	<button title={$t('submit_keys')} class="save" on:click={processCrypto}
		><i class="symbol">done</i><Tx text="submit" /></button
	>
</Modal>

<Header>
	<div title={$t('survey_title')} class="title" in:slide={{ duration: 200, easing: cubicInOut }}>
		{$title}
	</div>
</Header>

<Content>
	{#if keys.length === 1 || keys.length === 2}
		<p title={$t('survey_not_secure_title')} class="warning">
			<i class="symbol">warning</i><Tx text="survey_not_secure" />
			{keys.length === 1 ? $t('only_respondent') : $t('two_respondents')}
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
		<AnswerError
			{unansweredRequired}
			{questionIndex}
			--margin-top={question.type === 'text' ? '-2.5em' : ''}
		/>
	{/each}
</Content>

<Footer>
	<button title={$t('submit_survey')} class="footer-button done" on:click={submitSurvey}>
		<i class="symbol">done</i><Tx text="submit" />
	</button>
</Footer>

<style>
	.file-div {
		width: 100%;
	}

	.warning {
		margin: 0em 0em 0.5em 0em;
	}

	@media screen and (max-width: 768px) {
		.footer-button.done {
			font-size: 1.25em;
		}
	}
</style>
