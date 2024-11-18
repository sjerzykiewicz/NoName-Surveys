<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import Input from '$lib/components/global/Input.svelte';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let questionIndex: number;
	export let questionTypeData: { title: string; icon: string; text: string };
	export let questionInput: HTMLDivElement;

	function moveQuestionUp() {
		const higher = $questions[questionIndex];
		$questions[questionIndex] = $questions[questionIndex - 1];
		$questions[questionIndex - 1] = higher;
	}

	function moveQuestionDown() {
		const lower = $questions[questionIndex];
		$questions[questionIndex] = $questions[questionIndex + 1];
		$questions[questionIndex + 1] = lower;
	}

	function toggleRequirement() {
		$questions[questionIndex].required = !$questions[questionIndex].required;
	}

	function removeQuestion() {
		$questions.splice(questionIndex, 1);
		$questions = $questions;
	}

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

<div class="question-label" transition:slide={{ duration: 200, easing: cubicInOut }}>
	<div title={$t('question_index', { index: questionIndex + 1 })} class="index">
		{questionIndex + 1}.
	</div>
	<div title={$t(questionTypeData.title)} class="type">
		<i class="symbol">{questionTypeData.icon}</i><Tx text={questionTypeData.text} />
	</div>
</div>
<div class="question-area" transition:slide={{ duration: 200, easing: cubicInOut }}>
	<div class="arrows">
		<button
			title={$t('question_up')}
			class="up"
			disabled={questionIndex === 0}
			on:click={moveQuestionUp}
		>
			<i class="symbol">keyboard_arrow_up</i>
		</button>
		<button
			title={$t('question_down')}
			class="down"
			disabled={questionIndex === $questions.length - 1}
			on:click={moveQuestionDown}
		>
			<i class="symbol">keyboard_arrow_down</i>
		</button>
	</div>
	<Input
		bind:text={$questions[questionIndex].question}
		label={$t('question_label')}
		title={$t('question_title')}
		bind:element={questionInput}
	/>
	<button
		class="required-button tooltip"
		class:checked={$questions[questionIndex].required}
		on:click={toggleRequirement}
	>
		<i class="symbol">asterisk</i>
		<span class="tooltip-text top"
			>{$questions[questionIndex].required
				? $t('question_required')
				: $t('question_not_required')}</span
		>
	</button>
	<button title={$t('question_remove')} class="remove-question" on:click={removeQuestion}>
		<i class="symbol">delete</i>
	</button>
</div>

<style>
	.tooltip {
		--tooltip-width: 7.25em;
	}

	.required-button {
		margin-right: 0.5em;
		cursor: pointer;
		transition:
			0.2s,
			outline 0s;
	}

	.required-button .tooltip-text {
		cursor: help;
	}

	.required-button.checked {
		background-color: var(--accent-color-1);
		color: var(--text-color-2);
	}

	.required-button.checked:hover {
		background-color: var(--accent-color-2);
	}

	.required-button.checked:active {
		background-color: var(--border-color-1);
	}
</style>
