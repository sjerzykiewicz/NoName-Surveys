<script lang="ts">
	import { goto } from '$app/navigation';
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
	import Binary from '$lib/components/create-page/Binary.svelte';
	import List from '$lib/components/create-page/List.svelte';
	import Multi from '$lib/components/create-page/Multi.svelte';
	import Rank from '$lib/components/create-page/Rank.svelte';
	import Scale from '$lib/components/create-page/Scale.svelte';
	import Single from '$lib/components/create-page/Single.svelte';
	import Slider from '$lib/components/create-page/Slider.svelte';
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
	import type Question from '$lib/entities/questions/Question';
	import { getDraft } from '$lib/utils/getDraft';
	import {
		errorModalContent,
		isErrorModalHidden,
		isWarningModalHidden,
		LIMIT_OF_SURVEYS,
		S,
		warningModalContent
	} from '$lib/stores/global';
	import { getErrorMessage } from '$lib/utils/getErrorMessage';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';
	import { formatDateTime } from '$lib/utils/formatDate';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let drafts: {
		id: number;
		title: string;
		creation_date: string;
	}[];
	export let selectedDraftsToRemove: number[] = [];
	export let numSurveys: number;
	export let isExportButtonVisible: boolean = false;
	export let isRespondentModalHidden: boolean = true;

	$: draftIds = drafts.map((d) => d.id);

	$: allSelected =
		selectedDraftsToRemove.length === draftIds.length && selectedDraftsToRemove.length > 0;

	function toggleAll() {
		selectedDraftsToRemove = allSelected ? [] : [...draftIds];
	}

	async function loadDraft() {
		$draftStructure = getDraft($title.title, $questions);
		await goto('/create');
	}

	async function fetchDraft(draft: { id: number; title: string }) {
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
								(q as SliderQuestion).max_value.toString(),
								(q as SliderQuestion).precision.toString()
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
	}

	async function createSurvey() {
		if (numSurveys >= $LIMIT_OF_SURVEYS) {
			isExportButtonVisible = false;
			$warningModalContent = $t('limit_reached', { items: $t('surveys_genitive') });
			$isWarningModalHidden = false;
			return;
		}

		isRespondentModalHidden = false;
	}

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

{#if drafts.length === 0}
	<div class="info-row">
		<div title={$t('drafts')} class="title empty"><Tx text="no_drafts_yet" /></div>
		<div class="tooltip">
			<i class="symbol">info</i>
			<span class="tooltip-text {innerWidth <= $S ? 'bottom' : 'right'}">
				<Tx text="draft_tooltip" />
			</span>
		</div>
	</div>
{:else}
	<table>
		<tr>
			<th title={$t('select_all')} class="checkbox-entry" class:disabled={drafts.length === 0}
				><label
					><input
						type="checkbox"
						disabled={drafts.length === 0}
						on:change={toggleAll}
						checked={allSelected}
					/></label
				></th
			>
			<th title={$t('draft_title')} id="title-header"><Tx text="draft_title" /></th>
			<th title={$t('creation_date')} id="date-header"><Tx text="creation_date" /></th>
			<th title={$t('create')} id="create-header"><Tx text="create" /></th>
		</tr>
		{#each drafts as draft}
			<tr>
				<td title="{$t('select')} {draft.title}" class="checkbox-entry"
					><label>
						<input type="checkbox" bind:group={selectedDraftsToRemove} value={draft.id} />
					</label></td
				>
				<td title="{$t('open')} {draft.title}" class="title-entry"
					><button
						on:click={async () => {
							await fetchDraft(draft);
							await loadDraft();
						}}>{draft.title}</button
					></td
				>
				<td title={$t('creation_date')} class="date-entry">{formatDateTime(draft.creation_date)}</td
				>
				<td title="{$t('finish')} {draft.title}" class="button-entry"
					><button
						on:click={async () => {
							await fetchDraft(draft);
							await createSurvey();
						}}><i class="symbol">check_circle</i></button
					></td
				>
			</tr>
		{/each}
	</table>
{/if}

<style>
	.button-entry i {
		color: var(--accent-color-1);
		font-variation-settings: 'wght' 700;
	}

	#date-header {
		width: 22%;
		text-align: center;
	}

	@media screen and (max-width: 768px) {
		#date-header {
			width: 34%;
		}
	}
</style>
