<script lang="ts">
	import { goto, invalidateAll } from '$app/navigation';
	import { QuestionError } from '$lib/entities/QuestionError';
	import type { BinaryQuestion } from '$lib/entities/questions/Binary';
	import type { ListQuestion } from '$lib/entities/questions/List';
	import type { MultiQuestion } from '$lib/entities/questions/Multi';
	import type { RankQuestion } from '$lib/entities/questions/Rank';
	import type { SingleQuestion } from '$lib/entities/questions/Single';
	import type { SliderQuestion } from '$lib/entities/questions/Slider';
	import type { TextQuestion } from '$lib/entities/questions/Text';
	import { title, questions, currentDraftId, draft } from '$lib/stores/create-page';
	import Binary from '../create-page/Binary.svelte';
	import List from '../create-page/List.svelte';
	import Multi from '../create-page/Multi.svelte';
	import Rank from '../create-page/Rank.svelte';
	import Scale from '../create-page/Scale.svelte';
	import Single from '../create-page/Single.svelte';
	import Slider from '../create-page/Slider.svelte';
	import Text from '../create-page/Text.svelte';
	import SinglePreview from '../create-page/preview/SinglePreview.svelte';
	import MultiPreview from '../create-page/preview/MultiPreview.svelte';
	import ScalePreview from '../create-page/preview/ScalePreview.svelte';
	import SliderPreview from '../create-page/preview/SliderPreview.svelte';
	import ListPreview from '../create-page/preview/ListPreview.svelte';
	import RankPreview from '../create-page/preview/RankPreview.svelte';
	import BinaryPreview from '../create-page/preview/BinaryPreview.svelte';
	import TextPreview from '../create-page/preview/TextPreview.svelte';
	import { page } from '$app/stores';
	import type Question from '$lib/entities/questions/Question';
	import { getDraft } from '$lib/utils/getDraft';

	export let drafts: {
		id: number;
		title: string;
		creation_date: string;
	}[];

	function deleteDraft(i: number) {
		fetch('/api/surveys/drafts/delete', {
			method: 'POST',
			body: JSON.stringify({ user_email: $page.data.session?.user?.email, id: drafts[i].id }),
			headers: {
				'Content-Type': 'application/json'
			}
		})
			.then(() => {
				$title = '';
				$questions = [];
				drafts.splice(i, 1);
				invalidateAll();
			})
			.catch(() => alert('Error deleting draft'));
	}

	function loadDraft(i: number) {
		fetch('/api/surveys/drafts/fetch', {
			method: 'POST',
			body: JSON.stringify({ user_email: $page.data.session?.user?.email, id: drafts[i].id }),
			headers: {
				'Content-Type': 'application/json'
			}
		})
			.then(async (response) => {
				const body = await response.json();
				$currentDraftId = drafts[i].id;
				$title = drafts[i].title;
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
									error: QuestionError.NoError
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
									error: QuestionError.NoError
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
									error: QuestionError.NoError
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
									error: QuestionError.NoError
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
									error: QuestionError.NoError
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
									error: QuestionError.NoError
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
									error: QuestionError.NoError
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
									error: QuestionError.NoError
								}
							];
							break;
					}
				});
				$draft = getDraft($title, $questions);
				goto('/create');
			})
			.catch(() => alert('Error loading draft'));
	}

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

{#if drafts.length === 0}
	<div class="info-row">
		<div title="Drafts" class="title empty">No drafts yet!</div>
		<div class="tooltip">
			<i class="material-symbols-rounded">info</i>
			<span class="tooltip-text {innerWidth <= 423 ? 'bottom' : 'right'}">
				When creating a survey, you can save it as a draft for later use. To create a survey, click
				on the "Create" tab at the top of the page or the button below. All your saved drafts will
				be stored on this page.
			</span>
		</div>
	</div>
{:else}
	<table>
		<tr>
			<th title="Draft title" id="title-header">Draft Title</th>
			<th title="Creation date" id="date-header" colspan="2">Date</th>
		</tr>
		{#each drafts as draft, draftIndex}
			<tr>
				<td title="Open the draft" class="title-entry" on:click={() => loadDraft(draftIndex)}
					>{draft.title}</td
				>
				<td title="Creation date" class="date-entry">{draft.creation_date}</td>
				<td title="Delete the draft" class="button-entry" on:click={() => deleteDraft(draftIndex)}>
					<i class="material-symbols-rounded">delete</i></td
				>
			</tr>
		{/each}
	</table>
{/if}
<button title="Create a draft" on:click={() => goto('/create')}>
	<i class="material-symbols-rounded">add</i>Draft
</button>

<style>
	button {
		font-size: 1.25em;
		margin-top: 0.5em;
	}

	button i {
		margin-right: 0.15em;
		font-variation-settings: 'wght' 700;
	}

	#date-header {
		width: 24%;
	}

	@media screen and (max-width: 767px) {
		button {
			font-size: 1em;
		}
		#date-header {
			width: 39%;
		}
	}
</style>
