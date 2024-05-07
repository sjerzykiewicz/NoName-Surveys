<script lang="ts">
	import { questions } from '$lib/stores/create-page';

	export let questionIndex: number;

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

<div class="question-area">
	<div class="index">{questionIndex + 1}.</div>
	<div class="arrows">
		<button
			title="Move question up"
			class="up create-page-button"
			disabled={questionIndex === 0}
			on:click={moveQuestionUp}
		>
			<i class="material-symbols-rounded">arrow_drop_up</i>
		</button>
		<button
			title="Move question down"
			class="down create-page-button"
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
	>
		{$questions[questionIndex].question}
	</div>
	<button
		title={$questions[questionIndex].required ? 'Required' : 'Not required'}
		class="required-button create-page-button"
		class:checked={$questions[questionIndex].required}
		on:click={toggleRequirement}
	>
		<i class="material-symbols-rounded">asterisk</i>
	</button>
	<button class="create-page-button" title="Remove question" on:click={removeQuestion}>
		<i class="material-symbols-rounded">close</i>
	</button>
</div>

<style>
	.question-area {
		display: flex;
		flex-flow: row;
		align-items: center;
		margin-bottom: 1em;
		font-size: 1.25em;
		font-weight: normal;
		color: var(--text-color);
	}

	.question-input[contenteditable]:empty::before {
		content: 'Enter question...';
		color: var(--text-dark-color);
	}

	.index {
		margin-right: 0.3em;
		font-size: 1.1em;
		cursor: default;
		width: 1.4em;
		text-align: right;
	}

	.required-button {
		margin-right: 0.5em;
	}

	.required-button i {
		font-variation-settings: 'wght' 400;
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

	button {
		font-size: 1em;
	}

	i {
		font-variation-settings: 'wght' 700;
	}

	@media screen and (max-width: 767px) {
		.question-area,
		.index,
		button {
			font-size: 1em;
		}

		.arrows i {
			font-size: 1.2em;
		}

		.index {
			width: 2em;
		}
	}
</style>
