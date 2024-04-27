<script lang="ts">
	import { questions } from '$lib/components/create-page/stores';

	export let questionIndex: number;
	questionIndex += 1;

	function removeQuestion() {
		$questions.splice(questionIndex - 1, 1);
		$questions = $questions;
	}

	function moveQuestionUp() {
		const question = $questions[questionIndex - 1];
		$questions[questionIndex - 1] = $questions[questionIndex - 2];
		$questions[questionIndex - 2] = question;
		$questions = $questions;
	}

	function moveQuestionDown() {
		const question = $questions[questionIndex - 1];
		$questions[questionIndex - 1] = $questions[questionIndex];
		$questions[questionIndex] = question;
		$questions = $questions;
	}

	function toggleRequirement() {
		$questions[questionIndex - 1].required = !$questions[questionIndex - 1].required;
		$questions = $questions;
	}
</script>

<div class="question-area">
	<div class="index">{questionIndex}.</div>
	<div class="arrows">
		<button
			title="Move question up"
			class="up"
			disabled={questionIndex === 1}
			on:click={moveQuestionUp}
		>
			<i class="material-symbols-rounded">arrow_drop_up</i>
		</button>
		<button
			title="Move question down"
			class="down"
			disabled={questionIndex === $questions.length}
			on:click={moveQuestionDown}
		>
			<i class="material-symbols-rounded">arrow_drop_down</i>
		</button>
	</div>
	<div
		title="Enter question"
		class="question-input"
		contenteditable
		bind:textContent={$questions[questionIndex - 1].question}
	>
		{$questions[questionIndex - 1].question}
	</div>
	<button
		title={$questions[questionIndex - 1].required ? 'Required' : 'Not required'}
		class="required-button"
		class:checked={$questions[questionIndex - 1].required}
		on:click={toggleRequirement}
	>
		<i class="material-symbols-rounded">asterisk</i>
	</button>
	<button title="Remove question" on:click={removeQuestion}>
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
		font-family: 'Jura';
		color: #eaeaea;
	}

	.question-input {
		flex: 1;
		background-color: #1a1a1a;
		padding: 0.25em;
		border: 1px solid #999999;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		cursor: text;
		overflow: hidden;
		margin-right: 0.5em;
	}

	.question-input[contenteditable]:empty::before {
		content: 'Enter question...';
		color: #eaeaea40;
	}

	.index {
		margin-right: 0.3em;
		font-size: 1.1em;
		cursor: default;
		width: 1.4em;
		text-align: right;
	}

	.arrows {
		display: flex;
		flex-flow: column;
		margin-right: 0.5em;
	}

	.arrows i {
		line-height: 0.696em;
		overflow: hidden;
	}

	.up {
		border-radius: 5px 5px 0px 0px;
		border-bottom: 1px solid #999999;
		padding: 0em 0.25em 0em 0.25em;
	}

	.up:disabled {
		background-color: #1a1a1a;
		cursor: not-allowed;
	}

	.down {
		border-radius: 0px 0px 5px 5px;
		border-top: 0px;
		padding: 0em 0.25em 0em 0.25em;
	}

	.down:disabled {
		background-color: #1a1a1a;
		cursor: not-allowed;
	}

	.required-button {
		margin-right: 0.5em;
	}

	.required-button i {
		font-variation-settings: 'wght' 400;
	}

	.required-button.checked {
		background-color: #0075ff;
	}

	.required-button.checked:hover {
		background-color: #001c53;
	}

	.required-button.checked:active {
		background-color: #999999;
	}

	button {
		display: flex;
		background-color: #4a4a4a;
		padding: 0.25em;
		border: 1px solid #999999;
		border-radius: 5px;
		box-shadow: 0px 4px 4px #1a1a1a;
		font-size: 1em;
		font-family: 'Jura';
		color: #eaeaea;
		cursor: pointer;
		transition: background-color 0.2s;
	}

	button:hover {
		background-color: #1a1a1a;
	}

	button:active {
		background-color: #999999;
	}

	i {
		font-size: 1.15em;
		font-variation-settings: 'wght' 700;
	}

	@media screen and (max-width: 767px) {
		.question-area,
		.question-input,
		.index,
		button {
			font-size: 1em;
		}

		.arrows i {
			font-size: 1.2em;
		}
	}
</style>
