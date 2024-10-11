<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { handleNewLine } from '$lib/utils/handleNewLine';
	import { LIMIT_OF_CHARS } from '$lib/stores/global';
	import { limitInput } from '$lib/utils/limitInput';

	export let questionIndex: number;
</script>

<div
	class="choice-area"
	in:slide={{ delay: 200, duration: 200, easing: cubicInOut }}
	out:slide={{ duration: 200, easing: cubicInOut }}
>
	<div class="details">
		<div
			class="input-container"
			class:max={$questions[questionIndex].choices[0].length >= $LIMIT_OF_CHARS}
		>
			<div
				title="Enter question details"
				class="details-input"
				contenteditable
				bind:textContent={$questions[questionIndex].choices[0]}
				role="textbox"
				tabindex="0"
				on:keydown={(e) => {
					handleNewLine(e);
					limitInput(e, $questions[questionIndex].choices[0], $LIMIT_OF_CHARS);
				}}
			>
				{$questions[questionIndex].choices[0]}
			</div>
			<span class="char-count"
				>{$questions[questionIndex].choices[0].length} / {$LIMIT_OF_CHARS}</span
			>
		</div>
	</div>
</div>

<style>
	.details {
		display: flex;
	}

	.details-input {
		margin-right: 0em;
	}

	.details-input[contenteditable]:empty::before {
		content: 'Enter question details...';
	}

	.input-container {
		margin-bottom: -1.4em;
	}

	.char-count {
		left: 80%;
		font-size: 0.56em;
	}

	@media screen and (max-width: 767px) {
		.char-count {
			left: 65%;
			font-size: 0.5em;
		}
	}
</style>
