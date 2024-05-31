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

	export let structure: Survey;
	export let creationDate: string;

	function loadDraft() {
		$title = structure.title;
		$questions = [];
		structure.questions.forEach((q) => {
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

<div class="entry">
	<div class="data">
		<div class="entry-title">{structure.title}</div>
		<div class="entry-code">
			Created on: {creationDate}
		</div>
	</div>
	<div class="buttons">
		<button title="Open draft" class="open-button" on:click={loadDraft}>Open</button>
	</div>
</div>

<style>
	.entry {
		border: 1px solid var(--border-color);
		border-radius: 10px;
		color: var(--text-color);
		padding: 5px;
		padding-left: 10px;
		margin: 5px;
		margin-bottom: 15px;
		display: flex;
		justify-content: space-between;
	}

	.entry-title {
		color: var(--text-color);
		font-weight: bold;
		font-size: 1.5em;
		width: 100%;
		text-decoration: none;
	}

	.open-button {
		font-size: 1.25em;
		margin: 5px;
	}
</style>
