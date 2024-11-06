<script lang="ts">
	import { goto, invalidateAll } from '$app/navigation';
	import { SurveyError } from '$lib/entities/SurveyError';
	import type { BinaryQuestion } from '$lib/entities/questions/Binary';
	import type { ListQuestion } from '$lib/entities/questions/List';
	import type { MultiQuestion } from '$lib/entities/questions/Multi';
	import type { RankQuestion } from '$lib/entities/questions/Rank';
	import type { SingleQuestion } from '$lib/entities/questions/Single';
	import type { SliderQuestion } from '$lib/entities/questions/Slider';
	import type { TextQuestion } from '$lib/entities/questions/Text';
	import type { NumberQuestion } from '$lib/entities/questions/Number';
	import { title, questions, currentDraftId, draftStructure } from '$lib/stores/create-page';
	import Binary from '../create-page/Binary.svelte';
	import List from '../create-page/List.svelte';
	import Multi from '../create-page/Multi.svelte';
	import Rank from '../create-page/Rank.svelte';
	import Scale from '../create-page/Scale.svelte';
	import Single from '../create-page/Single.svelte';
	import Slider from '../create-page/Slider.svelte';
	import Text from '../create-page/Text.svelte';
	import Number from '../create-page/Number.svelte';
	import SinglePreview from '../create-page/preview/SinglePreview.svelte';
	import MultiPreview from '../create-page/preview/MultiPreview.svelte';
	import ScalePreview from '../create-page/preview/ScalePreview.svelte';
	import SliderPreview from '../create-page/preview/SliderPreview.svelte';
	import ListPreview from '../create-page/preview/ListPreview.svelte';
	import RankPreview from '../create-page/preview/RankPreview.svelte';
	import BinaryPreview from '../create-page/preview/BinaryPreview.svelte';
	import TextPreview from '../create-page/preview/TextPreview.svelte';
	import NumberPreview from '../create-page/preview/NumberPreview.svelte';
	import type Question from '$lib/entities/questions/Question';
	import { getDraft } from '$lib/utils/getDraft';
	import { errorModalContent, isErrorModalHidden, S } from '$lib/stores/global';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import DeleteModal from '$lib/components/global/DeleteModal.svelte';
	import PageButtons from '../global/PageButtons.svelte';

	export let drafts: {
		id: number;
		title: string;
		creation_date: string;
	}[];

	let selectedDraftsToRemove: typeof drafts = [];
	let isModalHidden: boolean = true;

	$: allSelected =
		selectedDraftsToRemove.length === drafts.length && selectedDraftsToRemove.length > 0;

	function toggleAll() {
		selectedDraftsToRemove = allSelected ? [] : [...drafts];
	}

	function formatDate(isoString: string): string {
		return new Date(isoString).toLocaleString();
	}

	async function deleteDrafts() {
		selectedDraftsToRemove.forEach(async (draft, i) => {
			const response = await fetch('/api/surveys/drafts/delete', {
				method: 'POST',
				body: JSON.stringify({ id: draft.id }),
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

			drafts.splice(i, 1);
		});

		isModalHidden = true;
		$title.title = '';
		$questions = [];
		selectedDraftsToRemove = [];
		invalidateAll();
	}

	async function loadDraft(draft: { id: number; title: string }) {
		const response = await fetch('/api/surveys/drafts/fetch', {
			method: 'POST',
			body: JSON.stringify({ id: draft.id }),
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
		$currentDraftId = draft.id;
		$title.title = draft.title;
		$questions = [];
		body.survey_structure.questions.forEach((q: Question) => {
			switch (q.question_type) {
				case 'single':
					$questions = [
						...$questions,
						{
							component: Single,
							preview: SinglePreview,
							required: q.required,
							question: q.question,
							choices: (q as SingleQuestion).choices,
							error: SurveyError.NoError
						}
					];
					break;
				case 'multi':
					$questions = [
						...$questions,
						{
							component: Multi,
							preview: MultiPreview,
							required: q.required,
							question: q.question,
							choices: (q as MultiQuestion).choices,
							error: SurveyError.NoError
						}
					];
					break;
				case 'list':
					$questions = [
						...$questions,
						{
							component: List,
							preview: ListPreview,
							required: q.required,
							question: q.question,
							choices: (q as ListQuestion).choices,
							error: SurveyError.NoError
						}
					];
					break;
				case 'rank':
					$questions = [
						...$questions,
						{
							component: Rank,
							preview: RankPreview,
							required: q.required,
							question: q.question,
							choices: (q as RankQuestion).choices,
							error: SurveyError.NoError
						}
					];
					break;
				case 'binary':
					$questions = [
						...$questions,
						{
							component: Binary,
							preview: BinaryPreview,
							required: q.required,
							question: q.question,
							choices: (q as BinaryQuestion).choices,
							error: SurveyError.NoError
						}
					];
					break;
				case 'scale':
					$questions = [
						...$questions,
						{
							component: Scale,
							preview: ScalePreview,
							required: q.required,
							question: q.question,
							choices: ['1', '2', '3', '4', '5'],
							error: SurveyError.NoError
						}
					];
					break;
				case 'slider':
					$questions = [
						...$questions,
						{
							component: Slider,
							preview: SliderPreview,
							required: q.required,
							question: q.question,
							choices: [
								(q as SliderQuestion).min_value.toString(),
								(q as SliderQuestion).max_value.toString()
							],
							error: SurveyError.NoError
						}
					];
					break;
				case 'number':
					$questions = [
						...$questions,
						{
							component: Number,
							preview: NumberPreview,
							required: q.required,
							question: q.question,
							choices: [
								(q as NumberQuestion).min_value.toString(),
								(q as NumberQuestion).max_value.toString()
							],
							error: SurveyError.NoError
						}
					];
					break;
				case 'text':
					$questions = [
						...$questions,
						{
							component: Text,
							preview: TextPreview,
							required: q.required,
							question: q.question,
							choices: [(q as TextQuestion).details],
							error: SurveyError.NoError
						}
					];
					break;
			}
		});
		$draftStructure = getDraft($title.title, $questions);
		goto('/create');
	}

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

<DeleteModal title="Deleting Drafts" bind:isHidden={isModalHidden} deleteEntries={deleteDrafts} />

{#if drafts.length === 0}
	<div class="info-row">
		<div title="Drafts" class="title empty">No drafts yet!</div>
		<div class="tooltip">
			<i class="material-symbols-rounded">info</i>
			<span class="tooltip-text {innerWidth <= $S ? 'bottom' : 'right'}">
				When creating a survey, you can save it as a draft for later use. To create a survey, click
				on the "Create" tab at the top of the page or the button below. All your saved drafts will
				be stored on this page.
			</span>
		</div>
	</div>
{:else}
	<table>
		<tr>
			<th title="Select all" class="checkbox-entry" class:disabled={drafts.length === 0}
				><label
					><input
						type="checkbox"
						disabled={drafts.length === 0}
						on:change={toggleAll}
						checked={allSelected}
					/></label
				></th
			>
			<th title="Draft title" id="title-header">Draft Title</th>
			<th title="Creation date" id="date-header">Creation Date</th>
		</tr>
		{#each drafts as draft}
			<tr>
				<td title="Select {draft.title}" class="checkbox-entry"
					><label>
						<input type="checkbox" bind:group={selectedDraftsToRemove} value={draft} />
					</label></td
				>
				<td title="Open the draft" class="title-entry"
					><button on:click={() => loadDraft(draft)}>{draft.title}</button></td
				>
				<td title="Creation date" class="date-entry">{formatDate(draft.creation_date)}</td>
			</tr>
		{/each}
	</table>
{/if}
<div class="button-row">
	<div class="button-sub-row">
		<button title="Create a draft" class="add-draft" on:click={() => goto('/create')}>
			<i class="material-symbols-rounded">add</i>Draft
		</button>
		{#if drafts.length > 0}
			<button
				title="Delete selected drafts"
				class="delete-draft"
				disabled={selectedDraftsToRemove.length === 0}
				on:click={() => (isModalHidden = false)}
			>
				<i class="material-symbols-rounded">delete</i>Delete
			</button>
		{/if}
	</div>
	<PageButtons />
</div>

<style>
	#date-header {
		width: 19%;
	}

	@media screen and (max-width: 768px) {
		#date-header {
			width: 33%;
		}
	}
</style>
