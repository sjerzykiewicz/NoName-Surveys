<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { handleNewLine } from '$lib/utils/handleNewLine';
	import { LIMIT_OF_CHARS } from '$lib/stores/global';
	import { limitInput } from '$lib/utils/limitInput';

	export let questionIndex: number;

	$questions[questionIndex].choices[1] = '';
</script>

<div
	class="choice-area display"
	in:slide={{ duration: 200, easing: cubicInOut }}
	out:slide={{ delay: 200, duration: 200, easing: cubicInOut }}
>
	<div title="Question details" class="details">
		{$questions[questionIndex].choices[0]}
	</div>
	<div
		class="input-container"
		class:max={$questions[questionIndex].choices[1].length > $LIMIT_OF_CHARS}
	>
		<div
			title="Enter your answer"
			class="text-area"
			contenteditable
			bind:textContent={$questions[questionIndex].choices[1]}
			role="textbox"
			tabindex="0"
			on:keydown={(e) => {
				handleNewLine(e);
				limitInput(e, $questions[questionIndex].choices[0], $LIMIT_OF_CHARS);
			}}
		>
			{$questions[questionIndex].choices[1]}
		</div>
		<span class="char-count">{$questions[questionIndex].choices[1].length} / {$LIMIT_OF_CHARS}</span
		>
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
