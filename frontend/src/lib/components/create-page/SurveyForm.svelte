<script lang="ts">
	import {
		questions,
		title,
		isDraftPopupVisible,
		currentDraftId,
		draft
	} from '$lib/stores/create-page';
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
	import { error } from '@sveltejs/kit';
	import { delay } from '$lib/utils/delay';
	import { getDraft } from '$lib/utils/getDraft';
	import Modal from '$lib/components/Modal.svelte';

	export let users: string[];
	export let groups: string[];
	export let isPreview: boolean;
	export let cryptoError: boolean;
	export let isDraftModalHidden: boolean = true;

	let questionInput: HTMLDivElement;

	async function saveDraft(overwrite: boolean) {
		const parsedSurvey = new Survey($title, constructQuestionList($questions));
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
				error(deleteResponse.status, { message: await deleteResponse.json() });
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
			error(createResponse.status, { message: await createResponse.json() });
		} else {
			const allResponse = await fetch('/api/surveys/drafts/all', {
				method: 'POST',
				body: JSON.stringify({ user_email: $page.data.session?.user?.email }),
				headers: {
					'Content-Type': 'application/json'
				}
			});

			if (!allResponse.ok) {
				error(allResponse.status, { message: await allResponse.json() });
			} else {
				const body = await allResponse.json();
				$currentDraftId = body[body.length - 1].id;
				$draft = getDraft($title, $questions);
				$isDraftPopupVisible = true;
				await delay(2000);
				$isDraftPopupVisible = false;
			}
		}
	}
</script>

<Modal icon="save" title="Save Draft" bind:isHidden={isDraftModalHidden}>
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
