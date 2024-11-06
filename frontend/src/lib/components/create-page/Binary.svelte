<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { handleNewLine } from '$lib/utils/handleNewLine';
	import { LIMIT_OF_CHARS } from '$lib/stores/global';
	import { limitInput } from '$lib/utils/limitInput';

	export let questionIndex: number;
</script>

<div class="choice-area binary" transition:slide={{ duration: 200, easing: cubicInOut }}>
	<label class="choice binary">
		<div class="icon">
			<input type="radio" disabled name={questionIndex.toString()} />
			<i class="material-symbols-rounded">thumb_up</i>
		</div>
		<div
			class="input-container"
			class:max={$questions[questionIndex].choices[0].length > $LIMIT_OF_CHARS}
		>
			<div
				title="Enter positive choice"
				class="choice-input yes binary"
				contenteditable
				role="textbox"
				tabindex="0"
				bind:textContent={$questions[questionIndex].choices[0]}
				on:keydown|once={() => ($questions[questionIndex].choices[0] = '')}
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
	</label>
	<label class="choice binary">
		<div class="icon">
			<input type="radio" disabled name={questionIndex.toString()} />
			<i class="material-symbols-rounded">thumb_down</i>
		</div>
		<div
			class="input-container"
			class:max={$questions[questionIndex].choices[1].length > $LIMIT_OF_CHARS}
		>
			<div
				title="Enter negative choice"
				class="choice-input no binary"
				contenteditable
				role="textbox"
				tabindex="0"
				bind:textContent={$questions[questionIndex].choices[1]}
				on:keydown|once={() => ($questions[questionIndex].choices[1] = '')}
				on:keydown={(e) => {
					handleNewLine(e);
					limitInput(e, $questions[questionIndex].choices[1], $LIMIT_OF_CHARS);
				}}
			>
				{$questions[questionIndex].choices[1]}
			</div>
			<span class="char-count"
				>{$questions[questionIndex].choices[1].length} / {$LIMIT_OF_CHARS}</span
			>
		</div>
	</label>
</div>

<style>
	.choice-area {
		justify-content: space-between;
		width: calc(86% - 2.25em);
	}

	.choice-input {
		width: 12em;
	}

	input {
		cursor: default;
	}

	.yes[contenteditable]:empty::before {
		content: 'Enter positive choice...';
	}

	.no[contenteditable]:empty::before {
		content: 'Enter negative choice...';
	}

	i {
		font-size: 1em;
		color: var(--border-color);
		cursor: default;
	}

	.input-container {
		flex: none;
	}

	.char-count {
		left: 30%;
	}

	@media screen and (max-width: 768px) {
		.choice-area {
			width: 86%;
		}

		.choice {
			width: 100%;
		}

		.char-count {
			left: 65%;
		}
	}
</style>
