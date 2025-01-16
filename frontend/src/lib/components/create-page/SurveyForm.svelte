<script lang="ts">
	import { questions, title, currentDraftId, draftStructure } from '$lib/stores/create-page';
	import Subtitle from '$lib/components/create-page/Subtitle.svelte';
	import SubtitlePreview from '$lib/components/create-page/preview/SubtitlePreview.svelte';
	import QuestionTitle from '$lib/components/create-page/QuestionTitle.svelte';
	import QuestionTitlePreview from '$lib/components/create-page/preview/QuestionTitlePreview.svelte';
	import QuestionError from './QuestionError.svelte';
	import ChoiceError from './ChoiceError.svelte';
	import AddQuestionButtons from '$lib/components/create-page/AddQuestionButtons.svelte';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { scrollToElement } from '$lib/utils/scrollToElement';
	import { getQuestionTypeData } from '$lib/utils/getQuestionTypeData';
	import Survey from '$lib/entities/surveys/Survey';
	import DraftCreateInfo from '$lib/entities/surveys/DraftCreateInfo';
	import { constructQuestionList } from '$lib/utils/constructQuestionList';
	import { getDraft } from '$lib/utils/getDraft';
	import Modal from '$lib/components/global/Modal.svelte';
	import QrCodeModal from '$lib/components/global/QrCodeModal.svelte';
	import { popup } from '$lib/utils/popup';
	import {
		errorModalContent,
		isErrorModalHidden,
		S,
		M,
		LIMIT_OF_DRAFTS,
		warningModalContent,
		isWarningModalHidden,
		LIMIT_OF_CHARS
	} from '$lib/stores/global';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import { invalidateAll } from '$app/navigation';
	import RespondentModal from './RespondentModal.svelte';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext, tick } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';
	import { SurveyError } from '$lib/entities/SurveyError';
	import { checkQuestionError } from '$lib/utils/checkQuestionError';
	import SubtitleError from './SubtitleError.svelte';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);
	let { options } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let users: string[];
	export let groups: string[];
	export let numDrafts: number;
	export let isPreview: boolean;
	export let isDraftModalHidden: boolean = true;
	export let isRespondentModalHidden: boolean = true;
	export let invalidEmails: string[] = [];
	export let isExportButtonVisible: boolean = false;
	export let ringMembers: string[] = [];
	export let selectedGroups: string[] = [];
	export let useCrypto: boolean = false;

	let questionInput: HTMLDivElement;
	let isSurveyModalHidden: boolean = true;
	let surveyCode: string;
	let isInfoPinned: boolean = false;

	const groupLink =
		'https://github.com/sjerzykiewicz/NoName-Surveys?tab=readme-ov-file#create-a-user-group';

	$: currentLang = $options.currentLang;

	async function addSubtitle() {
		const i: number = $questions.length - 1;
		if (i >= 0) checkQuestionError($questions[i], $LIMIT_OF_CHARS);

		$questions = [
			...$questions,
			{
				component: Subtitle,
				preview: SubtitlePreview,
				required: false,
				question: '',
				choices: [],
				error: SurveyError.NoError
			}
		];

		if (innerWidth > $M) {
			await tick();
			questionInput.focus();
			questionInput.scrollIntoView({ behavior: 'smooth', block: 'center' });
		}
	}

	async function saveDraft(overwrite: boolean) {
		isDraftModalHidden = true;

		if (
			(overwrite && numDrafts > $LIMIT_OF_DRAFTS) ||
			(!overwrite && numDrafts >= $LIMIT_OF_DRAFTS)
		) {
			isExportButtonVisible = false;
			$warningModalContent = $t('limit_reached', { items: $t('drafts_genitive') });
			$isWarningModalHidden = false;
			return;
		}

		if (overwrite) {
			const deleteResponse = await fetch('/api/surveys/drafts/delete', {
				method: 'POST',
				body: JSON.stringify({ ids: [$currentDraftId] }),
				headers: {
					'Content-Type': 'application/json'
				}
			});

			if (!deleteResponse.ok) {
				const body = await deleteResponse.json();
				$errorModalContent = getErrorMessage(body.detail);
				$isErrorModalHidden = false;
				return;
			}
		}

		const parsedSurvey = new Survey(constructQuestionList($questions));
		const draftInfo = new DraftCreateInfo($title.title, parsedSurvey);

		const createResponse = await fetch('/api/surveys/drafts/create', {
			method: 'POST',
			body: JSON.stringify(draftInfo),
			headers: {
				'Content-Type': 'application/json'
			}
		});

		if (!createResponse.ok) {
			const body = await createResponse.json();
			$errorModalContent = getErrorMessage(body.detail);
			$isErrorModalHidden = false;
			return;
		}

		$currentDraftId = await createResponse.json();
		$draftStructure = getDraft($title.title, $questions);
		popup('draft-popup');
		await invalidateAll();
	}

	async function handleEnter(event: KeyboardEvent) {
		if (!isDraftModalHidden && event.key === 'Enter') {
			event.preventDefault();
			event.stopImmediatePropagation();
			await saveDraft(false);
		}
	}

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />
<svelte:body on:keydown={handleEnter} />

<Modal
	icon="save"
	title={$t('saving_draft')}
	bind:isHidden={isDraftModalHidden}
	--width={innerWidth <= $M ? '20em' : '24em'}
>
	<span slot="content"><Tx text="saving_draft_alert" /></span>
	<button title={$t('overwrite_draft')} class="save" on:click={async () => await saveDraft(true)}
		><i class="symbol">save_as</i><Tx text="overwrite_draft" /></button
	>
	<button title={$t('save_new_draft')} class="save" on:click={async () => await saveDraft(false)}
		><i class="symbol">save</i><Tx text="save_new_draft" /></button
	>
</Modal>

<RespondentModal
	bind:isHidden={isRespondentModalHidden}
	bind:users
	bind:groups
	bind:invalidEmails
	bind:isExportButtonVisible
	bind:ringMembers
	bind:selectedGroups
	bind:useCrypto
	bind:isSurveyModalHidden
	bind:surveyCode
	isFromDraft={false}
/>

<QrCodeModal bind:isHidden={isSurveyModalHidden} title={$t('survey_success')} {surveyCode} />

{#each $questions as question, questionIndex (question)}
	<div
		class="question"
		id={`q${questionIndex}`}
		in:slide={{ duration: 200, easing: cubicInOut }}
		on:introend={() => scrollToElement('.add-question')}
	>
		{#if isPreview}
			{#if question.component === Subtitle}
				<SubtitlePreview {questionIndex} />
			{:else}
				<QuestionTitlePreview
					{questionIndex}
					questionTypeData={getQuestionTypeData(question.component)}
				/>
				<svelte:component this={question.preview} {questionIndex} />
			{/if}
		{:else if question.component === Subtitle}
			<Subtitle {questionIndex} bind:questionInput />
			<SubtitleError {questionIndex} />
		{:else}
			<QuestionTitle
				{questionIndex}
				questionTypeData={getQuestionTypeData(question.component)}
				bind:questionInput
			/>
			<QuestionError {questionIndex} />
			<svelte:component this={question.component} {questionIndex} />
			<ChoiceError {questionIndex} />
		{/if}
	</div>
{/each}
{#if !isPreview}
	<div class="button-row" transition:slide={{ duration: 200, easing: cubicInOut }}>
		<div class="button-sub-row">
			<button class="add-subtitle" on:click={addSubtitle}
				><i class="symbol">add</i><Tx text="subtitle" /></button
			>
			{#if innerWidth > $M}
				<button
					class="tooltip clickable hotkeys-info"
					on:click={() => (isInfoPinned = !isInfoPinned)}
				>
					<i class="symbol" class:fill={isInfoPinned}>bolt</i>
					{#if isInfoPinned}
						<span class="tooltip-text top">
							<Tx text="hotkeys_unpin" />
						</span>
						<span
							class="tooltip-text none"
							style="--tooltip-width: {currentLang === 'en' ? '28em' : '31em'}"
						>
							<Tx html="hotkeys_info" />
						</span>
					{:else}
						<span class="tooltip-text top">
							<Tx text="hotkeys_pin" />
						</span>
						<span
							class="tooltip-text right"
							style="--tooltip-width: {currentLang === 'en' ? '28em' : '31em'}"
						>
							<Tx html="hotkeys_info" />
						</span>
					{/if}
				</button>
			{/if}
			<div class="tooltip hoverable create-info">
				<i class="symbol">help</i>
				<span class="tooltip-text {innerWidth <= $S ? 'bottom' : 'right'}"
					><Tx text="create_groups_info" /><a href={groupLink} target="_blank"
						><Tx text="read_more" /></a
					></span
				>
			</div>
		</div>
	</div>
	<div class="button-row" transition:slide={{ duration: 200, easing: cubicInOut }}>
		<div class="button-sub-row">
			<AddQuestionButtons {questionInput} />
		</div>
	</div>
{/if}

<style>
	.hotkeys-info.tooltip {
		font-size: 1.5em;
	}

	.hotkeys-info.tooltip i {
		text-shadow: var(--shadow);
		transition: 0.2s;
	}

	.hotkeys-info.tooltip .tooltip-text {
		font-size: 0.6em;
		z-index: 2;
	}

	.hotkeys-info.tooltip .tooltip-text.top {
		--tooltip-width: 9em;
	}

	.hotkeys-info.tooltip .tooltip-text.right,
	.hotkeys-info.tooltip .tooltip-text.none {
		text-align: left;
		top: 445%;
	}

	.hotkeys-info.tooltip .tooltip-text.right::after {
		top: 7%;
	}

	.hotkeys-info.tooltip .tooltip-text.none {
		left: 700%;
		transform: translateY(-50%);
		visibility: visible !important;
		opacity: 1 !important;
	}

	.fill {
		font-variation-settings: 'FILL' 1;
	}

	.create-info.tooltip {
		--tooltip-width: 20em;
		font-size: 1.5em;
	}

	.create-info.tooltip .tooltip-text {
		text-align: left;
		font-size: 0.67em;
		z-index: 2;
	}

	.create-info.tooltip .tooltip-text.right {
		top: 234%;
	}

	.create-info.tooltip .tooltip-text.right::after {
		top: 12.5%;
	}

	.button-row {
		align-items: center;
		font-size: 1em;
		margin-top: 0em;
		margin-bottom: 0.5em;
	}

	.add-subtitle {
		font-size: 1.25em;
	}

	.add-subtitle i {
		margin-right: 0.15em;
		font-variation-settings: 'wght' 700;
	}

	@media screen and (max-width: 768px) {
		.create-info.tooltip {
			--tooltip-width: 12em;
			font-size: 1.25em;
		}

		.create-info.tooltip .tooltip-text.right {
			top: 367%;
		}

		.create-info.tooltip .tooltip-text.right::after {
			top: 7.5%;
		}

		.create-info.tooltip .tooltip-text.bottom {
			left: -60%;
		}

		.create-info.tooltip .tooltip-text.bottom::after {
			left: 65%;
		}

		.add-subtitle {
			font-size: 1em;
		}
	}
</style>
