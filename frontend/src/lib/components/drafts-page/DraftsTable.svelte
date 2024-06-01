<script lang="ts">
	import { goto } from '$app/navigation';
	import { QuestionError } from '$lib/entities/QuestionError';
	import type { BinaryQuestion } from '$lib/entities/questions/Binary';
	import type { ListQuestion } from '$lib/entities/questions/List';
	import type { MultiQuestion } from '$lib/entities/questions/Multi';
	import type { RankQuestion } from '$lib/entities/questions/Rank';
	import type { SingleQuestion } from '$lib/entities/questions/Single';
	import type { SliderQuestion } from '$lib/entities/questions/Slider';
	import type { TextQuestion } from '$lib/entities/questions/Text';
	import type Survey from '$lib/entities/surveys/Survey';
	import { title, questions } from '$lib/stores/create-page';
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

	export let drafts: {
		creator: number;
		survey_structure: Survey;
		creation_date: string;
	}[];

	function loadDraft(i: number) {
		$title = drafts[i].survey_structure.title;
		$questions = [];
		drafts[i].survey_structure.questions.forEach((q) => {
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
		goto('/create');
	}
</script>

<table>
	<tr>
		<th title="Draft title" id="title-header">Draft Title</th>
		<th title="Creation date" id="date-header">Date</th>
	</tr>
	{#each drafts as draft, draftIndex}
		<tr>
			<td title="Click to open draft" class="title-entry" on:click={() => loadDraft(draftIndex)}
				>{draft.survey_structure.title}</td
			>
			<td title="Creation date" class="date-entry">{draft.creation_date}</td>
		</tr>
	{/each}
</table>

<style>
	table {
		width: 100%;
		border: 1px solid var(--border-color);
		border-collapse: separate;
		border-spacing: 0;
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--shadow-color);
		font-size: 1.25em;
		color: var(--text-color);
	}

	th,
	td {
		padding: 0.25em;
		text-align: left;
		text-shadow: 0px 4px 4px var(--shadow-color);
	}

	th {
		background-color: var(--secondary-dark-color);
		font-weight: bold;
		cursor: default;
		overflow-wrap: break-word;
	}

	td {
		overflow-wrap: anywhere;
	}

	tr:nth-child(2n + 1) td {
		background-color: var(--primary-dark-color);
	}

	tr:nth-child(2n + 2) td {
		background-color: var(--primary-color);
	}

	tr:first-of-type {
		border-radius: 4px 4px 0px 0px;
	}

	tr:last-of-type {
		border-radius: 0px 0px 4px 4px;
	}

	th:first-of-type {
		border-top-left-radius: 4px;
	}

	th:last-of-type {
		border-top-right-radius: 4px;
	}

	tr:last-of-type td:first-of-type {
		border-bottom-left-radius: 4px;
	}

	tr:last-of-type td:last-of-type {
		border-bottom-right-radius: 4px;
	}

	#title-header {
		width: 82%;
	}

	.title-entry {
		cursor: pointer;
	}

	.title-entry:hover {
		background-color: var(--secondary-color);
	}

	.title-entry:active {
		background-color: var(--border-color);
	}

	#date-header {
		width: 18%;
	}

	.date-entry {
		cursor: default;
	}

	@media screen and (max-width: 767px) {
		table {
			font-size: 0.8em;
		}

		#title-header {
			width: 74%;
		}

		#date-header {
			width: 26%;
		}
	}
</style>
