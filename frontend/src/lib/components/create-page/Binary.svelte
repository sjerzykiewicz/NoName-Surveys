<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { handleNewLine } from '$lib/utils/handleNewLine';

	export let questionIndex: number;
</script>

<div
	class="choice-area binary"
	in:slide={{ delay: 200, duration: 200, easing: cubicInOut }}
	out:slide={{ duration: 200, easing: cubicInOut }}
>
	<label class="choice binary">
		<div class="icon">
			<input type="radio" disabled name={questionIndex.toString()} />
			<i class="material-symbols-rounded">thumb_up</i>
		</div>
		<div
			title="Enter positive choice"
			class="choice-input yes binary"
			contenteditable
			role="textbox"
			tabindex="0"
			bind:textContent={$questions[questionIndex].choices[0]}
			on:keydown|once={() => ($questions[questionIndex].choices[0] = '')}
			on:keydown={handleNewLine}
		>
			{$questions[questionIndex].choices[0]}
		</div>
	</label>
	<label class="choice binary">
		<div class="icon">
			<input type="radio" disabled name={questionIndex.toString()} />
			<i class="material-symbols-rounded">thumb_down</i>
		</div>
		<div
			title="Enter negative choice"
			class="choice-input no binary"
			contenteditable
			role="textbox"
			tabindex="0"
			bind:textContent={$questions[questionIndex].choices[1]}
			on:keydown|once={() => ($questions[questionIndex].choices[1] = '')}
			on:keydown={handleNewLine}
		>
			{$questions[questionIndex].choices[1]}
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

	@media screen and (max-width: 767px) {
		.choice-area {
			width: 86%;
		}

		.choice {
			width: 100%;
		}
	}
</style>
