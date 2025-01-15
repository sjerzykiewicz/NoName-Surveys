<script lang="ts">
	import Single from '$lib/components/create-page/Single.svelte';
	import Multi from '$lib/components/create-page/Multi.svelte';
	import Scale from '$lib/components/create-page/Scale.svelte';
	import Slider from '$lib/components/create-page/Slider.svelte';
	import List from '$lib/components/create-page/List.svelte';
	import Rank from '$lib/components/create-page/Rank.svelte';
	import Binary from '$lib/components/create-page/Binary.svelte';
	import Text from '$lib/components/create-page/Text.svelte';
	import Number from '$lib/components/create-page/Number.svelte';
	import SinglePreview from '$lib/components/create-page/preview/SinglePreview.svelte';
	import MultiPreview from '$lib/components/create-page/preview/MultiPreview.svelte';
	import ScalePreview from '$lib/components/create-page/preview/ScalePreview.svelte';
	import SliderPreview from '$lib/components/create-page/preview/SliderPreview.svelte';
	import ListPreview from '$lib/components/create-page/preview/ListPreview.svelte';
	import RankPreview from '$lib/components/create-page/preview/RankPreview.svelte';
	import BinaryPreview from '$lib/components/create-page/preview/BinaryPreview.svelte';
	import TextPreview from '$lib/components/create-page/preview/TextPreview.svelte';
	import NumberPreview from '$lib/components/create-page/preview/NumberPreview.svelte';
	import Subtitle from '$lib/components/create-page/Subtitle.svelte';
	import SubtitlePreview from '$lib/components/create-page/preview/SubtitlePreview.svelte';
	import { questions } from '$lib/stores/create-page';
	import { type ComponentType, tick } from 'svelte';
	import { slide } from 'svelte/transition';
	import { cubicInOut } from 'svelte/easing';
	import QuestionTypeButton from './QuestionTypeButton.svelte';
	import { SurveyError } from '$lib/entities/SurveyError';
	import { scrollToElement } from '$lib/utils/scrollToElement';
	import { previousQuestion } from '$lib/stores/create-page';
	import { getQuestionTypeData } from '$lib/utils/getQuestionTypeData';
	import { LIMIT_OF_CHARS } from '$lib/stores/global';
	import { M } from '$lib/stores/global';
	import { checkQuestionError } from '$lib/utils/checkQuestionError';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);
	let { options } = getContext<SvelteTranslate>(CONTEXT_KEY);

	$: currentLang = $options.currentLang;

	export let questionInput: HTMLDivElement;

	let isPanelVisible: boolean = false;
	let questionTypes: Array<ComponentType> = [
		Text,
		Number,
		Single,
		Multi,
		Binary,
		Scale,
		Slider,
		List,
		Rank
	];

	function getPreviewComponent(component: ComponentType) {
		switch (component) {
			case Single:
				return SinglePreview;
			case Multi:
				return MultiPreview;
			case Scale:
				return ScalePreview;
			case Slider:
				return SliderPreview;
			case List:
				return ListPreview;
			case Rank:
				return RankPreview;
			case Binary:
				return BinaryPreview;
			case Number:
				return NumberPreview;
			case Text:
				return TextPreview;
			default:
				return SubtitlePreview;
		}
	}

	function togglePanel() {
		isPanelVisible = !isPanelVisible;
	}

	function setQuestionChoices(component: ComponentType) {
		if ([Single, Multi, List, Rank].includes(component)) {
			return ['', ''];
		} else if (component === Scale) {
			return ['1', '2', '3', '4', '5'];
		} else if (component === Binary) {
			return [$t('binary_yes'), $t('binary_no')];
		} else if (component === Slider) {
			return ['0', '10', '1'];
		} else if (component === Number) {
			return ['0', '10'];
		} else if (component === Text) {
			return [''];
		} else {
			return [];
		}
	}

	async function addQuestion(component: ComponentType) {
		const i: number = $questions.length - 1;
		if (i >= 0) checkQuestionError($questions[i], $LIMIT_OF_CHARS);

		const choices: Array<string> = setQuestionChoices(component);

		$questions = [
			...$questions,
			{
				component: component,
				preview: getPreviewComponent(component),
				required: false,
				question: '',
				choices: choices,
				error: SurveyError.NoError
			}
		];

		if (component !== Subtitle) {
			$previousQuestion = component;
			isPanelVisible = false;
		}

		if (innerWidth > $M) {
			await tick();
			questionInput.focus();
			questionInput.scrollIntoView({ behavior: 'smooth', block: 'center' });
		}
	}

	function focusPreviousInput() {
		const c = getClosestElement('choice');
		const q = getClosestElement('question');

		let element: HTMLElement | null = null;

		if (c && q) {
			if (c.index === 0) {
				element = document.getElementById(`q${q.index}`);
			} else {
				element = document.getElementById(`q${q.index}c${c.index - 1}`);
			}
		} else if (q) {
			if (q.index === 0) {
				element = document.getElementById('header');
			} else {
				if (
					$questions[q.index - 1].component === Scale ||
					$questions[q.index - 1].component === Subtitle
				) {
					element = document.getElementById(`q${q.index - 1}`);
				} else {
					element = document.getElementById(
						`q${q.index - 1}c${$questions[q.index - 1].choices.length - 1}`
					);
				}
			}
		} else {
			if (
				$questions[$questions.length - 1].component === Scale ||
				$questions[$questions.length - 1].component === Subtitle
			) {
				element = document.getElementById(`q${$questions.length - 1}`);
			} else {
				element = document.getElementById(
					`q${$questions.length - 1}c${$questions[$questions.length - 1].choices.length - 1}`
				);
			}
		}

		if (element) {
			const input = element.querySelector('.input');
			if (input && (input instanceof HTMLDivElement || input instanceof HTMLInputElement)) {
				input.focus();
				input.scrollIntoView({ behavior: 'smooth', block: 'center' });
			}
		}
	}

	function focusNextInput() {
		const c = getClosestElement('choice');
		const q = getClosestElement('question');

		let element: HTMLElement | null = null;

		if (c && q) {
			if (c.index === $questions[q.index].choices.length - 1) {
				if (q.index === $questions.length - 1) {
					element = document.getElementById('header');
				} else {
					element = document.getElementById(`q${q.index + 1}`);
				}
			} else {
				element = document.getElementById(`q${q.index}c${c.index + 1}`);
			}
		} else if (q) {
			if ($questions[q.index].component === Scale || $questions[q.index].component === Subtitle) {
				if (q.index === $questions.length - 1) {
					element = document.getElementById('header');
				} else {
					element = document.getElementById(`q${q.index + 1}`);
				}
			} else {
				element = document.getElementById(`q${q.index}c0`);
			}
		} else {
			element = document.getElementById(`q0`);
		}

		if (element) {
			const input = element.querySelector('.input');
			if (input && (input instanceof HTMLDivElement || input instanceof HTMLInputElement)) {
				input.focus();
				input.scrollIntoView({ behavior: 'smooth', block: 'center' });
			}
		}
	}

	function focusPreviousQuestion() {
		const q = getClosestElement('question');

		let element: HTMLElement | null = null;

		if (q) {
			if (q.index === 0) {
				element = document.getElementById(`q${$questions.length - 1}`);
			} else {
				element = document.getElementById(`q${q.index - 1}`);
			}
		}

		if (element) {
			const input = element.querySelector('.input');
			if (input && input instanceof HTMLDivElement) {
				input.focus();
				input.scrollIntoView({ behavior: 'smooth', block: 'center' });
			}
		}
	}

	function focusNextQuestion() {
		const q = getClosestElement('question');

		let element: HTMLElement | null = null;

		if (q) {
			if (q.index === $questions.length - 1) {
				element = document.getElementById(`q0`);
			} else {
				element = document.getElementById(`q${q.index + 1}`);
			}
		}

		if (element) {
			const input = element.querySelector('.input');
			if (input && input instanceof HTMLDivElement) {
				input.focus();
				input.scrollIntoView({ behavior: 'smooth', block: 'center' });
			}
		}
	}

	function focusTitle() {
		const element = document.getElementById('header');
		if (element) {
			const input = element.querySelector('.input');
			if (input && input instanceof HTMLDivElement) {
				input.focus();
				input.scrollIntoView({ behavior: 'smooth', block: 'center' });
			}
		}
	}

	function focusCreate() {
		const element = document.getElementById('create');
		if (element) {
			element.focus();
			element.scrollIntoView({ behavior: 'smooth', block: 'center' });
		}
	}

	async function moveQuestionUp() {
		const q = getClosestElement('question');
		if (!q || q.index === 0) return;

		const higher = $questions[q.index];
		$questions[q.index] = $questions[q.index - 1];
		$questions[q.index - 1] = higher;

		await tick();
		q.element.focus();
		q.element.scrollIntoView({ behavior: 'smooth', block: 'center' });
	}

	async function moveQuestionDown() {
		const q = getClosestElement('question');
		if (!q || q.index === $questions.length - 1) return;

		const lower = $questions[q.index];
		$questions[q.index] = $questions[q.index + 1];
		$questions[q.index + 1] = lower;

		await tick();
		q.element.focus();
		q.element.scrollIntoView({ behavior: 'smooth', block: 'center' });
	}

	function toggleRequirement() {
		const q = getClosestElement('question');
		if (!q) return;
		if ($questions[q.index].component === Subtitle) return;

		$questions[q.index].required = !$questions[q.index].required;
	}

	async function removeQuestionOrChoice() {
		const c = getClosestElement('choice');
		const q = getClosestElement('question');

		let element: HTMLElement | null = null;

		if (c && q) {
			if ($questions[q.index].choices.length > 2 && $questions[q.index].component !== Slider) {
				if (c.index === $questions[q.index].choices.length - 1) {
					element = document.getElementById(`q${q.index}c${c.index - 1}`);
				} else {
					element = document.getElementById(`q${q.index}c${c.index}`);
				}

				$questions[q.index].choices.splice(c.index, 1);
			}
		} else if (q) {
			if (q.index === $questions.length - 1) {
				element = document.getElementById(`q${q.index - 1}`);
			} else {
				element = document.getElementById(`q${q.index + 1}`);
			}

			$questions.splice(q.index, 1);
		} else {
			return;
		}

		$questions = $questions;

		await tick();
		if (element) {
			const input = element.querySelector('.input');
			if (input && input instanceof HTMLDivElement) {
				input.focus();
				input.scrollIntoView({ behavior: 'smooth', block: 'center' });
			}
		}
	}

	async function addChoice() {
		const q = getClosestElement('question');
		if (!q) return;

		$questions[q.index].choices = [...$questions[q.index].choices, ''];

		await tick();
		const element = document.getElementById(
			`q${q.index}c${$questions[q.index].choices.length - 1}`
		);
		if (element) {
			const input = element.querySelector('.input');
			if (input && (input instanceof HTMLDivElement || input instanceof HTMLInputElement)) {
				input.focus();
				input.scrollIntoView({ behavior: 'smooth', block: 'center' });
			}
		}
	}

	function getClosestElement(item: string) {
		const focusedElement = document.activeElement;
		if (!focusedElement) return null;
		if (
			!(
				focusedElement instanceof HTMLDivElement ||
				focusedElement instanceof HTMLInputElement ||
				focusedElement instanceof HTMLButtonElement
			)
		)
			return null;

		const itemElement = focusedElement.closest<HTMLDivElement>(`.${item}`);
		if (!itemElement) return null;

		const charIndex = itemElement.id.indexOf(item[0]);

		return { index: parseInt(itemElement.id.substring(charIndex + 1)), element: focusedElement };
	}

	function handleHotkeys(e: KeyboardEvent) {
		if (e.altKey) {
			const key = e.code;
			switch (key) {
				case 'Digit1':
				case 'Numpad1':
					addQuestion(questionTypes[0]);
					break;
				case 'Digit2':
				case 'Numpad2':
					addQuestion(questionTypes[1]);
					break;
				case 'Digit3':
				case 'Numpad3':
					addQuestion(questionTypes[2]);
					break;
				case 'Digit4':
				case 'Numpad4':
					addQuestion(questionTypes[3]);
					break;
				case 'Digit5':
				case 'Numpad5':
					addQuestion(questionTypes[4]);
					break;
				case 'Digit6':
				case 'Numpad6':
					addQuestion(questionTypes[5]);
					break;
				case 'Digit7':
				case 'Numpad7':
					addQuestion(questionTypes[6]);
					break;
				case 'Digit8':
				case 'Numpad8':
					addQuestion(questionTypes[7]);
					break;
				case 'Digit9':
				case 'Numpad9':
					addQuestion(questionTypes[8]);
					break;
				case 'Digit0':
				case 'Numpad0':
					if ($previousQuestion) addQuestion($previousQuestion);
					break;
				case 'Minus':
				case 'Equal':
				case 'NumpadSubtract':
					addQuestion(Subtitle);
					break;
				case 'ArrowLeft':
					focusPreviousQuestion();
					break;
				case 'ArrowRight':
					focusNextQuestion();
					break;
				case 'ArrowUp':
					focusPreviousInput();
					break;
				case 'ArrowDown':
					focusNextInput();
					break;
				case 'Home':
					focusTitle();
					break;
				case 'End':
					focusCreate();
					break;
				case 'PageUp':
					moveQuestionUp();
					break;
				case 'PageDown':
					moveQuestionDown();
					break;
				case 'Backquote':
				case 'Backslash':
				case 'NumpadMultiply':
				case 'NumpadDivide':
					toggleRequirement();
					break;
				case 'Backspace':
				case 'Delete':
				case 'NumpadDecimal':
					removeQuestionOrChoice();
					break;
				case 'Enter':
				case 'NumpadEnter':
				case 'Insert':
				case 'NumpadAdd':
					addChoice();
					break;
			}
			e.preventDefault();
			e.stopImmediatePropagation();
		}
	}

	function handleEscape(event: KeyboardEvent) {
		if (isPanelVisible && event.key === 'Escape') {
			isPanelVisible = false;
		}
	}

	function handleClick(event: MouseEvent) {
		if (isPanelVisible && !(event.target as HTMLElement).closest('.add-question')) {
			isPanelVisible = false;
		}
	}

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />
<svelte:body on:keydown|capture={handleHotkeys} on:keydown={handleEscape} on:click={handleClick} />

<div class="button-group" style="--width: {currentLang === 'en' ? '7.5em' : '8em'}">
	<div class="add-buttons">
		<button
			title={isPanelVisible ? $t('question_choose_type_stop') : $t('question_choose_type')}
			class="add-question"
			class:clicked={isPanelVisible}
			class:previous={$previousQuestion}
			on:click={togglePanel}
		>
			<div class="button-text"><i class="symbol add">add</i><Tx text="question" /></div>
			<i class="symbol arrow">arrow_drop_down</i>
		</button>
		{#if $previousQuestion}
			<QuestionTypeButton
				questionType={$previousQuestion}
				questionTypeData={getQuestionTypeData($previousQuestion)}
				questionTypeIndex={-1}
				on:addQuestionType={(event) => addQuestion(event.detail.component)}
			/>
		{/if}
	</div>
	{#if isPanelVisible}
		<div
			class="button-panel"
			transition:slide={{ duration: 200, easing: cubicInOut }}
			on:introstart={() => scrollToElement('.add-question')}
		>
			{#each questionTypes as questionType, questionTypeIndex}
				<QuestionTypeButton
					{questionType}
					questionTypeData={getQuestionTypeData(questionType)}
					{questionTypeIndex}
					on:addQuestionType={(event) => addQuestion(event.detail.component)}
				/>
			{/each}
		</div>
	{/if}
</div>

<style>
	.button-group {
		width: fit-content;
		font-size: 1.25em;
	}

	.add-buttons {
		display: flex;
		border-radius: 5px;
		box-shadow: var(--shadow);
	}

	.add-question {
		display: flex;
		justify-content: space-between;
		width: var(--width, 7.5em);
		box-shadow: none;
		transition:
			0.2s,
			outline 0s;
	}

	.button-text {
		display: flex;
		align-items: center;
	}

	.add-question.clicked {
		background-color: var(--primary-color-2);
		border-bottom-right-radius: 0px;
		border-bottom-left-radius: 0px;
	}

	.add-question.clicked:hover {
		background-color: var(--secondary-color-1);
	}

	.add-question.clicked:active {
		background-color: var(--border-color-1);
	}

	.add-question.previous {
		border-top-right-radius: 0px;
		border-bottom-right-radius: 0px;
	}

	.button-panel {
		display: flex;
		flex-flow: column;
		border-radius: 0px 0px 5px 5px;
		box-shadow: var(--shadow);
		width: var(--width, 7.5em);
		height: auto;
		position: absolute;
		z-index: 2;
	}

	.add-question.clicked .add {
		transform: rotate(45deg);
	}

	.add-question.clicked .arrow {
		transform: rotate(180deg);
	}

	.add-question .add {
		margin-right: 0.15em;
		font-variation-settings: 'wght' 700;
	}

	.add-question i {
		transform: rotate(0deg);
		transition: transform 0.2s;
	}

	@media screen and (max-width: 768px) {
		.button-group {
			font-size: 1em;
		}
	}
</style>
