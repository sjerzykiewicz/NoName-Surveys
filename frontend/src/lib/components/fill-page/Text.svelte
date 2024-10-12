<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';
	import { LIMIT_OF_CHARS } from '$lib/stores/global';
	import { handleNewLine } from '$lib/utils/handleNewLine';
	import { limitInput } from '$lib/utils/limitInput';

	export let questionIndex: number;

	$answers[questionIndex].choices[0] = '';
</script>

<div class="choice-area display">
	<div title="Question details" class="details">
		{$questions[questionIndex].choices[0]}
	</div>
	<div
		class="input-container"
		class:max={$answers[questionIndex].choices[0].length >= $LIMIT_OF_CHARS}
	>
		<div
			title="Enter your answer"
			class="text-area"
			contenteditable
			bind:textContent={$answers[questionIndex].choices[0]}
			role="textbox"
			tabindex="0"
			on:keydown={(e) => {
				handleNewLine(e);
				limitInput(e, $questions[questionIndex].choices[0], $LIMIT_OF_CHARS);
			}}
		>
			{$answers[questionIndex].choices[0]}
		</div>
		<span class="char-count">{$answers[questionIndex].choices[0].length} / {$LIMIT_OF_CHARS}</span>
	</div>
</div>

<style>
	.text-area {
		margin-right: 0em;
	}

	.text-area[contenteditable]:empty::before {
		content: 'Enter your answer...';
	}
</style>
