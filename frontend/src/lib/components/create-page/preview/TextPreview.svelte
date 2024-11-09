<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { handleNewLine } from '$lib/utils/handleNewLine';
	import { LIMIT_OF_CHARS } from '$lib/stores/global';
	import { limitInput } from '$lib/utils/limitInput';

	export let questionIndex: number;

	let text: string = '';
</script>

<div class="choice-area display" transition:slide={{ duration: 200, easing: cubicInOut }}>
	<div title="Question details" class="details">
		{$questions[questionIndex].choices[0]}
	</div>
	<div class="input-container" class:max={text.length > $LIMIT_OF_CHARS}>
		<div
			title="Enter your answer"
			class="text-input"
			contenteditable
			bind:textContent={text}
			role="textbox"
			tabindex="0"
			on:keydown={(e) => {
				handleNewLine(e);
				limitInput(e, $questions[questionIndex].choices[0], $LIMIT_OF_CHARS);
			}}
		>
			{text}
		</div>
		<span class="char-count">{text.length} / {$LIMIT_OF_CHARS}</span>
	</div>
</div>

<style>
	.text-input {
		margin-right: 0em;
	}
</style>
