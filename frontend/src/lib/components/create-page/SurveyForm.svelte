<script lang="ts">
	import {
		questions,
		title,
		currentDraftId,
		draftStructure,
		useCrypto,
		ringMembers,
		selectedGroup
	} from '$lib/stores/create-page';
	import QuestionTitle from '$lib/components/create-page/QuestionTitle.svelte';
	import QuestionTitlePreview from '$lib/components/create-page/preview/QuestionTitlePreview.svelte';
	import QuestionError from './QuestionError.svelte';
	import ChoiceError from './ChoiceError.svelte';
	import AddQuestionButtons from '$lib/components/create-page/AddQuestionButtons.svelte';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { scrollToElement } from '$lib/utils/scrollToElement';
	import { getQuestionTypeData } from '$lib/utils/getQuestionTypeData';
	import { page } from '$app/stores';
	import Survey from '$lib/entities/surveys/Survey';
	import SurveyCreateInfo from '$lib/entities/surveys/SurveyCreateInfo';
	import DraftCreateInfo from '$lib/entities/surveys/DraftCreateInfo';
	import { constructQuestionList } from '$lib/utils/constructQuestionList';
	import { getDraft } from '$lib/utils/getDraft';
	import { trimQuestions } from '$lib/utils/trimQuestions';
	import Modal from '$lib/components/global/Modal.svelte';
	import QrCodeModal from '$lib/components/global/QrCodeModal.svelte';
	import { popup } from '$lib/utils/popup';
	import { errorModalContent, isErrorModalHidden, S, M } from '$lib/stores/global';
	import SelectGroup from './SelectGroup.svelte';
	import SelectUsers from './SelectUsers.svelte';
	import CryptoError from './CryptoError.svelte';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import { onMount } from 'svelte';
	import ImportEmails from '$lib/components/global/ImportEmails.svelte';

	export let users: string[];
	export let groups: string[];
	export let isPreview: boolean;
	export let isDraftModalHidden: boolean = true;
	export let isRespondentModalHidden: boolean = true;

	let cryptoError: boolean = false;
	let questionInput: HTMLDivElement;
	let isSurveyModalHidden: boolean = true;
	let surveyCode: string;
	let ring: string[] = [];

	function checkCorrectness() {
		cryptoError = false;
		const g = $selectedGroup;
		const r = $ringMembers;
		if (
			$useCrypto &&
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

		$title.title = $title.title.trim();
		$questions = trimQuestions($questions);

		const parsedSurvey = new Survey(constructQuestionList($questions));
		const draftInfo = new DraftCreateInfo(
			$page.data.session!.user!.email!,
			$title.title,
			parsedSurvey
		);

		if (overwrite) {
			const deleteResponse = await fetch('/api/surveys/drafts/delete', {
				method: 'POST',
				body: JSON.stringify({ id: $currentDraftId }),
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
	}

	async function fetchGroup(name: string) {
		const response = await fetch('/api/groups/fetch', {
			method: 'POST',
			body: JSON.stringify({ name: name }),
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
		ring = [...$ringMembers, ...body];
	}

	async function createSurvey() {
		if (!checkCorrectness()) return;

		isRespondentModalHidden = true;

		const parsedSurvey = new Survey(constructQuestionList($questions));
		let finalRing: string[] = [];

		if ($selectedGroup.length > 0) {
			await fetchGroup($selectedGroup[0]);
			finalRing = [...new Set(ring)];
		} else if ($ringMembers.length > 0) {
			finalRing = [...$ringMembers];
		}

		const surveyInfo = new SurveyCreateInfo(
			$page.data.session!.user!.email!,
			$title.title,
			parsedSurvey,
			$useCrypto,
			finalRing
		);

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
		ring = [];
		finalRing = [];
		$useCrypto = false;
		$ringMembers = [];
		$selectedGroup = [];
		surveyCode = body.survey_code;
		isSurveyModalHidden = false;
	}

	let innerWidth: number;

	$: isCryptoDisabled = !$useCrypto;

	onMount(() => {
		function handleEnter(event: KeyboardEvent) {
			if (!isRespondentModalHidden && event.key === 'Enter') {
				event.preventDefault();
				createSurvey();
			}
		}

		document.body.addEventListener('keydown', handleEnter);

		return () => {
			document.body.removeEventListener('keydown', handleEnter);
		};
	});
</script>

<svelte:window bind:innerWidth />

<Modal icon="save" title="Saving Draft" bind:isHidden={isDraftModalHidden}>
	<span slot="content">Do you wish to overwrite the draft or save a new draft?</span>
	<button title="Overwrite draft" class="save" on:click={() => saveDraft(true)}
		>Overwrite Draft</button
	>
	<button title="Save new draft" class="save" on:click={() => saveDraft(false)}
		>Save New Draft</button
	>
</Modal>

<Modal
	icon="group"
	title="Define Respondent Group"
	bind:isHidden={isRespondentModalHidden}
	width={innerWidth <= $M ? 20 : 26}
>
	<div slot="content">
		<span>Do you wish to make the survey public or secure?</span>
		<div class="crypto-buttons">
			<button
				title="Public"
				class="access-button"
				class:save={!$useCrypto}
				on:click={() => ($useCrypto = false)}
			>
				<i class="material-symbols-rounded">public</i>Public
			</button>
			<button
				title="Secure"
				class="access-button"
				class:save={$useCrypto}
				on:click={() => ($useCrypto = true)}
			>
				<i class="material-symbols-rounded">encrypted</i>Secure
			</button>
		</div>
		<div class="select-box">
			<SelectGroup {groups} bind:disabled={isCryptoDisabled} />
			<div id="or" class:disabled={isCryptoDisabled}>Or</div>
			<SelectUsers {users} bind:disabled={isCryptoDisabled} />
			<CryptoError error={cryptoError} />
			<ImportEmails
				bind:users={$ringMembers}
				title="Import users from a .csv file"
				label="Or import users from a .csv file."
				id="emails-file"
				checkKeys={true}
				width="100%"
				bind:disabled={isCryptoDisabled}
			/>
		</div>
	</div>
	<button title="Define respondent group" class="save apply" on:click={createSurvey}
		><i class="material-symbols-rounded">done</i>Apply</button
	>
</Modal>

<QrCodeModal bind:isHidden={isSurveyModalHidden} title="Survey Created Successfully" {surveyCode} />

{#each $questions as question, questionIndex (question)}
	<div
		class="question"
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
		<AddQuestionButtons {questionInput} />
		<div class="tooltip create-info">
			<i class="material-symbols-rounded">info</i>
			<span class="tooltip-text {innerWidth <= $S ? 'bottom' : 'right'}"
				>Before creating a secure survey, consider setting up a user group. User groups make it easy
				to select the same set of respondents across multiple surveys. However, if you prefer, you
				can proceed without using them.</span
			>
		</div>
	</div>
{/if}

<style>
	.tooltip {
		--tooltip-width: 22em;
		font-size: 1.5em;
	}

	.tooltip .tooltip-text {
		font-size: 0.8em;
	}

	.button-row {
		align-items: center;
		font-size: 1em;
		margin-top: 0em;
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

	.apply i {
		font-variation-settings: 'wght' 700;
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
		color: var(--text-color);
		cursor: default;
	}

	#or.disabled {
		color: var(--text-dark-color) !important;
		cursor: not-allowed !important;
	}

	@media screen and (max-width: 768px) {
		.tooltip {
			--tooltip-width: 10em;
			font-size: 1.25em;
		}
	}
</style>
