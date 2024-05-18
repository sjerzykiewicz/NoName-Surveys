<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { getQuestionTypeData } from '$lib/utils/getQuestionTypeData';
	import { beforeUpdate, type ComponentType } from 'svelte';

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

<div class="question-label">
	<div title="Question no. {questionIndex + 1}" class="index">{questionIndex + 1}.</div>
	<div title={questionTypeData.title} class="type">
		<i class="material-symbols-rounded">{questionTypeData.icon}</i>{questionTypeData.text}
	</div>
</div>
<div class="question-area">
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
	>
		{$questions[questionIndex].question}
	</div>
	<button
		title={$questions[questionIndex].required ? 'Required' : 'Not required'}
		class="required-button"
		class:checked={$questions[questionIndex].required}
		on:click={toggleRequirement}
	>
		<i class="material-symbols-rounded">asterisk</i>
	</button>
	<button title="Remove question" class="remove-question" on:click={removeQuestion}>
		<i class="material-symbols-rounded">close</i>
	</button>
</div>

<style>
	.question-label {
		display: flex;
		flex-flow: row;
		align-items: center;
		margin-bottom: 0.25em;
		font-size: 1.25em;
		color: var(--border-color);
		cursor: default;
	}

	.question-label i {
		font-size: 1em;
		margin-right: 0.25em;
	}

	.type {
		display: flex;
		flex-flow: row;
		align-items: center;
	}

	.question-input[contenteditable]:empty::before {
		content: 'Enter question...';
		color: var(--text-dark-color);
	}

	.required-button {
		margin-right: 0.5em;
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

	.remove-question i {
		font-variation-settings: 'wght' 700;
	}

	@media screen and (max-width: 767px) {
		.question-label,
		button {
			font-size: 1em;
		}

		.arrows i {
			font-size: 1.2em;
		}
	}
</style>
