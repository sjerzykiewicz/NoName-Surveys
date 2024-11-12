<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import Input from '$lib/components/global/Input.svelte';

	export let questionIndex: number;
	export let questionTypeData: { title: string; icon: string; text: string };
	export let questionInput: HTMLDivElement;

	function removeQuestion() {
		$questions.splice(questionIndex, 1);
		$questions = $questions;
	}

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

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

<div
	class="question-label"
	id={questionIndex.toString()}
	transition:slide={{ duration: 200, easing: cubicInOut }}
>
	<div title="Question no. {questionIndex + 1}" class="index">{questionIndex + 1}.</div>
	<div title={questionTypeData.title} class="type">
		<i class="symbol">{questionTypeData.icon}</i>{questionTypeData.text}
	</div>
</div>
<div class="question-area" transition:slide={{ duration: 200, easing: cubicInOut }}>
	<div class="arrows">
		<button
			title="Move question up"
			class="up"
			disabled={questionIndex === 0}
			on:click={moveQuestionUp}
		>
			<i class="symbol">keyboard_arrow_up</i>
		</button>
		<button
			title="Move question down"
			class="down"
			disabled={questionIndex === $questions.length - 1}
			on:click={moveQuestionDown}
		>
			<i class="symbol">keyboard_arrow_down</i>
		</button>
	</div>
	<Input
		bind:text={$questions[questionIndex].question}
		label="Question"
		title="Enter a question"
		bind:element={questionInput}
	/>
	<button
		class="required-button tooltip"
		class:checked={$questions[questionIndex].required}
		on:click={toggleRequirement}
	>
		<i class="symbol">asterisk</i>
		<span class="tooltip-text top"
			>{$questions[questionIndex].required ? 'Required.' : 'Not required.'}</span
		>
	</button>
	<button title="Remove question" class="remove-question" on:click={removeQuestion}>
		<i class="symbol">delete</i>
	</button>
</div>

<style>
	.tooltip {
		--tooltip-width: 6.5em;
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
