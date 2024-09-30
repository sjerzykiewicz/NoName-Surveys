<script lang="ts">
	import {
		currentDraftId,
		questions,
		questionsCopy,
		title,
		titleCopy,
		isDraftModalHidden,
		isDraftPopupVisible
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
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import Survey from '$lib/entities/surveys/Survey';
	import DraftCreateInfo from '$lib/entities/surveys/DraftCreateInfo';
	import { constructQuestionList } from '$lib/utils/constructQuestionList';
	import { error } from '@sveltejs/kit';
	import { delay } from '$lib/utils/delay';

	export let users: string[];
	export let groups: string[];
	export let isPreview: boolean;
	export let cryptoError: boolean;

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
				$titleCopy = $title;
				$questionsCopy = JSON.parse(JSON.stringify($questions));
				$isDraftPopupVisible = true;
				await delay(2000);
				$isDraftPopupVisible = false;
			}
		}
	}

	onMount(() => {
		function handleEscape(event: KeyboardEvent) {
			if (!$isDraftModalHidden && event.key === 'Escape') {
				$isDraftModalHidden = true;
			}
		}

		document.body.addEventListener('keydown', handleEscape);

		return () => {
			document.body.removeEventListener('keydown', handleEscape);
		};
	});
</script>

<section class="overlay" class:hidden={$isDraftModalHidden}>
	<div class="modal">
		<div class="top">
			<div class="caption">
				<i class="material-symbols-rounded">help</i>Save Draft
			</div>
			<button title="Cancel" on:click={() => ($isDraftModalHidden = true)}>
				<i class="material-symbols-rounded">close</i>
			</button>
		</div>
		<div class="text">Do you wish to overwrite the draft or save a new draft?</div>
		<div class="buttons">
			<button
				title="Overwrite draft"
				class="save"
				on:click={() => {
					saveDraft(true);
					$isDraftModalHidden = true;
				}}>Overwrite Draft</button
			>
			<button
				title="Save new draft"
				class="save"
				on:click={() => {
					saveDraft(false);
					$isDraftModalHidden = true;
				}}>Save New Draft</button
			>
		</div>
	</div>
</section>

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
	.overlay {
		display: flex;
		justify-content: center;
		position: fixed;
		top: 0;
		bottom: 0;
		left: 0;
		right: 0;
		width: 100%;
		height: 100%;
		background: rgba(0, 0, 0, 0.5);
		backdrop-filter: blur(2px);
		z-index: 2;
		opacity: 1;
		transition: opacity 0.2s;
	}

	.overlay.hidden {
		visibility: hidden;
		opacity: 0;
	}

	.modal {
		display: flex;
		flex-direction: column;
		justify-content: center;
		top: 10%;
		width: 20em;
		position: absolute;
		background-color: var(--secondary-color);
		border: 1px solid var(--border-color);
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--shadow-color);
		font-size: 1.25em;
		color: var(--text-color);
		z-index: 3;
	}

	.modal div {
		display: flex;
	}

	.modal .top {
		align-items: center;
		justify-content: space-between;
		background-color: var(--secondary-dark-color);
		border-bottom: 1px solid var(--border-color);
		border-top-left-radius: 5px;
		border-top-right-radius: 5px;
		padding: 0.5em;
	}

	.modal .top .caption {
		align-items: center;
		font-weight: bold;
		font-size: 1.25em;
		text-shadow: 0px 4px 4px var(--shadow-color);
		cursor: default;
	}

	.modal .top .caption i {
		margin-right: 0.15em;
	}

	.modal .top button i {
		font-variation-settings: 'wght' 700;
	}

	.modal .text {
		justify-content: center;
		padding: 1em;
		text-align: center;
		text-shadow: 0px 4px 4px var(--shadow-color);
		cursor: default;
	}

	.modal .buttons {
		flex-flow: row;
		justify-content: space-around;
		padding-bottom: 1em;
	}

	.modal .buttons button {
		width: 8em;
		justify-content: center;
	}

	.button-row {
		display: flex;
		flex-flow: row wrap;
		align-items: flex-start;
		justify-content: flex-start;
		align-content: space-between;
	}
</style>
