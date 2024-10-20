<script lang="ts">
	import { questions, title, currentDraftId, draft } from '$lib/stores/create-page';
	import QuestionTitle from '$lib/components/create-page/QuestionTitle.svelte';
	import QuestionTitlePreview from '$lib/components/create-page/preview/QuestionTitlePreview.svelte';
	import QuestionError from './QuestionError.svelte';
	import ChoiceError from './ChoiceError.svelte';
	import AddQuestionButtons from '$lib/components/create-page/AddQuestionButtons.svelte';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { scrollToElement } from '$lib/utils/scrollToElement';
	import CryptoButtons from './CryptoButtons.svelte';
	import { getQuestionTypeData } from '$lib/utils/getQuestionTypeData';
	import { page } from '$app/stores';
	import Survey from '$lib/entities/surveys/Survey';
	import DraftCreateInfo from '$lib/entities/surveys/DraftCreateInfo';
	import { constructQuestionList } from '$lib/utils/constructQuestionList';
	import { getDraft } from '$lib/utils/getDraft';
	import { trimQuestions } from '$lib/utils/trimQuestions';
	import Modal from '$lib/components/Modal.svelte';
	import QrCodeModal from '$lib/components/QrCodeModal.svelte';
	import { popup } from '$lib/utils/popup';

	export let users: string[];
	export let groups: string[];
	export let isPreview: boolean;
	export let cryptoError: boolean;
	export let isDraftModalHidden: boolean = true;
	export let isSurveyModalHidden: boolean = true;
	export let surveyCode: string;

	let questionInput: HTMLDivElement;

	async function saveDraft(overwrite: boolean) {
		$title.title = $title.title.trim();
		$questions = trimQuestions($questions);

		const parsedSurvey = new Survey($title.title, constructQuestionList($questions));
		const draftInfo = new DraftCreateInfo($page.data.session!.user!.email!, parsedSurvey);

		if (overwrite) {
			const deleteResponse = await fetch('/api/surveys/drafts/delete', {
				method: 'POST',
				body: JSON.stringify({ user_email: $page.data.session?.user?.email, id: $currentDraftId }),
				headers: {
					'Content-Type': 'application/json'
				}
			});

			if (!deleteResponse.ok) {
				const body = await deleteResponse.json();
				alert(body.detail);
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
			alert(body.detail);
			return;
		}

		$currentDraftId = await createResponse.json();
		$draft = getDraft($title.title, $questions);
		popup('draft-popup');
	}
</script>

<Modal icon="save" title="Saving Draft" bind:isHidden={isDraftModalHidden}>
	<span slot="content">Do you wish to overwrite the draft or save a new draft?</span>
	<button
		title="Overwrite draft"
		class="save"
		on:click={() => {
			saveDraft(true);
			isDraftModalHidden = true;
		}}>Overwrite Draft</button
	>
	<button
		title="Save new draft"
		class="save"
		on:click={() => {
			saveDraft(false);
			isDraftModalHidden = true;
		}}>Save New Draft</button
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
	<div
		class="button-row"
		in:slide={{ delay: 200, duration: 200, easing: cubicInOut }}
		out:slide={{ duration: 200, easing: cubicInOut }}
	>
		<AddQuestionButtons {questionInput} />
		<CryptoButtons {users} {groups} {cryptoError} />
	</div>
{/if}

<style>
	.button-row {
		display: flex;
		flex-flow: row wrap;
		align-items: flex-start;
		justify-content: flex-start;
		align-content: space-between;
	}
</style>
