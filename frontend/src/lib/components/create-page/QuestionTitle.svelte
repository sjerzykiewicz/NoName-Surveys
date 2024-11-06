<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { handleNewLine } from '$lib/utils/handleNewLine';
	import { LIMIT_OF_CHARS } from '$lib/stores/global';
	import { limitInput } from '$lib/utils/limitInput';

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
		$questions = $questions;
	}
</script>

<div
	class="question-label"
	id={questionIndex.toString()}
	transition:slide={{ duration: 200, easing: cubicInOut }}
>
	<div title="Question no. {questionIndex + 1}" class="index">{questionIndex + 1}.</div>
	<div title={questionTypeData.title} class="type">
		<i class="material-symbols-rounded">{questionTypeData.icon}</i>{questionTypeData.text}
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
		class="input-container"
		class:max={$questions[questionIndex].question.length > $LIMIT_OF_CHARS}
	>
		<div
			title="Enter question"
			class="question-input"
			contenteditable
			bind:textContent={$questions[questionIndex].question}
			bind:this={questionInput}
			role="textbox"
			tabindex="0"
			on:keydown={(e) => {
				handleNewLine(e);
				limitInput(e, $questions[questionIndex].question, $LIMIT_OF_CHARS);
			}}
		>
			{$questions[questionIndex].question}
		</div>
		<span class="char-count">{$questions[questionIndex].question.length} / {$LIMIT_OF_CHARS}</span>
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

	.input-container {
		margin-bottom: -1.4em;
	}

	.char-count {
		left: 80%;
		font-size: 0.56em;
	}

	@media screen and (max-width: 768px) {
		.char-count {
			left: 65%;
			font-size: 0.5em;
		}
	}
</style>
