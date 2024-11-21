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
	import SurveyCreateInfo from '$lib/entities/surveys/SurveyCreateInfo';
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
	import SelectGroup from './SelectGroup.svelte';
	import SelectUsers from './SelectUsers.svelte';
	import CryptoError from './CryptoError.svelte';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import { onMount } from 'svelte';
	import ImportEmails from '$lib/components/global/ImportEmails.svelte';
	import { invalidateAll } from '$app/navigation';
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

	let cryptoError: boolean = false;
	let questionInput: HTMLDivElement;
	let isSurveyModalHidden: boolean = true;
	let surveyCode: string;

	function checkCorrectness() {
		cryptoError = false;
		const g = selectedGroups;
		const r = ringMembers;
		if (
			useCrypto &&
			(g === null || g === undefined || g.length === 0) &&
			(r === null || r === undefined || r.length === 0)
		) {
			cryptoError = true;
			return false;
		}
		return true;
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

	async function createSurvey() {
		if (!checkCorrectness()) return;

		isRespondentModalHidden = true;

		const parsedSurvey = new Survey(constructQuestionList($questions));
		const surveyInfo = new SurveyCreateInfo($title.title, parsedSurvey, useCrypto, ringMembers);

		const response = await fetch('/api/surveys/create', {
			method: 'POST',
			body: JSON.stringify(surveyInfo),
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

		const body = await response.json();
		useCrypto = false;
		ringMembers = [];
		selectedGroups = [];
		surveyCode = body.survey_code;
		isSurveyModalHidden = false;
		await invalidateAll();
	}

	let innerWidth: number;

	$: isCryptoDisabled = !useCrypto;

	onMount(() => {
		function handleEnterRespondent(event: KeyboardEvent) {
			if (!isRespondentModalHidden && event.key === 'Enter') {
				event.preventDefault();
				createSurvey();
				event.stopImmediatePropagation();
			}
		}

		function handleEnterDraft(event: KeyboardEvent) {
			if (!isDraftModalHidden && event.key === 'Enter') {
				event.preventDefault();
				saveDraft(false);
				event.stopImmediatePropagation();
			}
		}

		document.body.addEventListener('keydown', handleEnterRespondent);
		document.body.addEventListener('keydown', handleEnterDraft);

		return () => {
			document.body.removeEventListener('keydown', handleEnterRespondent);
			document.body.removeEventListener('keydown', handleEnterDraft);
		};
	});
</script>

<svelte:window bind:innerWidth />

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

<Modal
	icon="group"
	title={$t('define_respondent_group')}
	bind:isHidden={isRespondentModalHidden}
	--width={innerWidth <= $M ? '20em' : '26em'}
>
	<div slot="content">
		<span><Tx text="define_respondent_group_alert" /></span>
		<div class="crypto-buttons">
			<button
				title={$t('public')}
				class="access-button"
				class:save={!useCrypto}
				on:click={() => (useCrypto = false)}
			>
				<i class="symbol">public</i><Tx text="public" />
			</button>
			<button
				title={$t('secure')}
				class="access-button"
				class:save={useCrypto}
				on:click={() => (useCrypto = true)}
			>
				<i class="symbol">encrypted</i><Tx text="secure" />
			</button>
		</div>
		<div class="select-box" transition:slide={{ duration: 0.2, easing: cubicInOut }}>
			<SelectGroup {groups} bind:ringMembers bind:selectedGroups disabled={isCryptoDisabled} />
			<div id="or" class:disabled={isCryptoDisabled}><Tx text="or" /></div>
			<SelectUsers {users} bind:ringMembers disabled={isCryptoDisabled} />
			<CryptoError error={cryptoError} bind:ringMembers bind:selectedGroups bind:useCrypto />
			<div class="import">
				<ImportEmails
					bind:users={ringMembers}
					title={$t('import_users_title')}
					label={$t('import_users_label')}
					checkKeys={true}
					--width="100%"
					disabled={isCryptoDisabled}
					bind:invalidEmails
					bind:isExportButtonVisible
				/>
			</div>
		</div>
	</div>
	<button title={$t('define_respondent_group')} class="done" on:click={createSurvey}
		><i class="symbol">done</i><Tx text="create" /></button
	>
</Modal>

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
		--tooltip-width: 17em;
		font-size: 1.5em;
	}

	.create-info.tooltip .tooltip-text {
		text-align: left;
		font-size: 0.8em;
	}

	.button-row {
		align-items: center;
		font-size: 1em;
		margin-top: 0em;
	}

	.button-sub-row {
		gap: 0.5em;
	}

	.crypto-buttons {
		display: flex;
		flex-flow: row;
		justify-content: space-around;
		padding-top: 1em;
		padding-bottom: 1em;
	}

	.access-button {
		width: fit-content;
		justify-content: center;
		margin-right: 0.5em;
		margin-bottom: 0.5em;
	}

	.access-button i {
		margin-right: 0.15em;
	}

	.select-box {
		text-align: left;
	}

	#or {
		display: flex;
		flex-flow: row;
		align-items: flex-start;
		justify-content: flex-start;
		margin-bottom: 0.5em;
		font-size: 0.8em;
		color: var(--text-color-1);
		cursor: default;
		transition:
			0.2s,
			outline 0s;
	}

	#or.disabled {
		color: var(--text-color-3) !important;
		cursor: not-allowed !important;
	}

	.import {
		font-size: 0.8em;
	}

	@media screen and (max-width: 768px) {
		.create-info.tooltip {
			--tooltip-width: 10em;
			font-size: 1.25em;
		}

		.create-info.tooltip .tooltip-text.bottom {
			left: -250%;
		}

		.create-info.tooltip .tooltip-text.bottom::after {
			left: 90%;
		}

		.import {
			font-size: 1em;
		}
	}
</style>
