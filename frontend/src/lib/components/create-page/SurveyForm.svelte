<script lang="ts">
	import { questions, title, currentDraftId, draftStructure } from '$lib/stores/create-page';
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
		isWarningModalHidden
	} from '$lib/stores/global';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import { invalidateAll } from '$app/navigation';
	import RespondentModal from './RespondentModal.svelte';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

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

	function handleEnter(event: KeyboardEvent) {
		if (!isDraftModalHidden && event.key === 'Enter') {
			event.preventDefault();
			saveDraft(false);
			event.stopImmediatePropagation();
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
	<button title={$t('overwrite_draft')} class="save" on:click={() => saveDraft(true)}
		><i class="symbol">save_as</i><Tx text="overwrite_draft" /></button
	>
	<button title={$t('save_new_draft')} class="save" on:click={() => saveDraft(false)}
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
			<QuestionTitlePreview
				{questionIndex}
				questionTypeData={getQuestionTypeData(question.component)}
			/>
			<svelte:component this={question.preview} {questionIndex} />
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
			<AddQuestionButtons {questionInput} />
			<div class="tooltip create-info">
				<i class="symbol">info</i>
				<span class="tooltip-text {innerWidth <= $S ? 'bottom' : 'right'}"
					><Tx text="groups_info" /></span
				>
			</div>
		</div>
	</div>
{/if}

<style>
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
		top: 220%;
	}

	.create-info.tooltip .tooltip-text.right::after {
		top: 15%;
	}

	.button-row {
		align-items: center;
		font-size: 1em;
		margin-top: 0em;
	}

	@media screen and (max-width: 768px) {
		.create-info.tooltip {
			--tooltip-width: 12em;
			font-size: 1.25em;
		}

		.create-info.tooltip .tooltip-text.right {
			top: 350%;
		}

		.create-info.tooltip .tooltip-text.right::after {
			top: 10%;
		}

		.create-info.tooltip .tooltip-text.bottom {
			left: -175%;
		}

		.create-info.tooltip .tooltip-text.bottom::after {
			left: 80%;
		}
	}
</style>
