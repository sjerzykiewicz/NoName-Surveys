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
