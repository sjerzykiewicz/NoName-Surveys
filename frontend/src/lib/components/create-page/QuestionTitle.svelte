<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { getQuestionTypeData } from '$lib/utils/getQuestionTypeData';
	import { beforeUpdate, type ComponentType } from 'svelte';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { handleNewLine } from '$lib/utils/handleNewLine';

	export let questionIndex: number;
	export let questionType: ComponentType;

	let questionTypeData: { title: string; icon: string; text: string };

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
		$questions = $questions;
	}

	beforeUpdate(() => {
		questionTypeData = getQuestionTypeData(questionType);
	});
</script>

<div
	class="question-label"
	id={questionIndex.toString()}
	in:slide={{ delay: 200, duration: 200, easing: cubicInOut }}
	out:slide={{ duration: 200, easing: cubicInOut }}
>
	<div title="Question no. {questionIndex + 1}" class="index">{questionIndex + 1}.</div>
	<div title={questionTypeData.title} class="type">
		<i class="material-symbols-rounded">{questionTypeData.icon}</i>{questionTypeData.text}
	</div>
</div>
<div
	class="question-area"
	in:slide={{ delay: 200, duration: 200, easing: cubicInOut }}
	out:slide={{ duration: 200, easing: cubicInOut }}
>
	<div class="arrows">
		<button
			title="Move question up"
			class="up"
			disabled={questionIndex === 0}
			on:click={moveQuestionUp}
		>
			<i class="material-symbols-rounded">arrow_drop_up</i>
		</button>
		<button
			title="Move question down"
			class="down"
			disabled={questionIndex === $questions.length - 1}
			on:click={moveQuestionDown}
		>
			<i class="material-symbols-rounded">arrow_drop_down</i>
		</button>
	</div>
	<div
		title="Enter question"
		class="question-input"
		contenteditable
		bind:textContent={$questions[questionIndex].question}
		role="textbox"
		tabindex="0"
		on:keydown={handleNewLine}
	>
		{$questions[questionIndex].question}
	</div>
	<button
		class="required-button tooltip"
		class:checked={$questions[questionIndex].required}
		on:click={toggleRequirement}
	>
		<i class="material-symbols-rounded">asterisk</i>
		<span class="tooltip-text top"
			>{$questions[questionIndex].required ? 'Required.' : 'Not required.'}</span
		>
	</button>
	<button title="Remove question" class="remove-question" on:click={removeQuestion}>
		<i class="material-symbols-rounded">close</i>
	</button>
</div>

<style>
	.tooltip {
		--tooltip-width: 6.5em;
	}

	.question-input[contenteditable]:empty::before {
		content: 'Enter question...';
		color: var(--text-dark-color);
	}

	.required-button {
		margin-right: 0.5em;
		cursor: pointer;
	}

	.required-button .tooltip-text {
		cursor: help;
	}

	.required-button.checked {
		background-color: var(--accent-color);
		color: var(--text-color-2);
	}

	.required-button.checked:hover {
		background-color: var(--accent-dark-color);
	}

	.required-button.checked:active {
		background-color: var(--border-color);
	}

	.remove-question i {
		font-variation-settings: 'wght' 700;
	}
</style>
