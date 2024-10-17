<script lang="ts">
	import { title } from '$lib/stores/create-page';
	import { M } from '$lib/stores/global';
	import { handleNewLine } from '$lib/utils/handleNewLine';
	import { limitInput } from '$lib/utils/limitInput';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { LIMIT_OF_CHARS } from '$lib/stores/global';

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

<div class="input-container" class:max={$title.title.length > $LIMIT_OF_CHARS}>
	<!-- svelte-ignore a11y-autofocus -->
	<div
		title="Enter survey title"
		class="title-input"
		id="title"
		contenteditable
		bind:textContent={$title.title}
		autofocus={innerWidth > $M && $title.title.length === 0}
		role="textbox"
		tabindex="0"
		on:keydown={(e) => {
			handleNewLine(e);
			limitInput(e, $title.title, $LIMIT_OF_CHARS);
		}}
		in:slide={{ delay: 200, duration: 200, easing: cubicInOut }}
		out:slide={{ duration: 200, easing: cubicInOut }}
	>
		{$title.title}
	</div>
	<span class="char-count">{$title.title.length} / {$LIMIT_OF_CHARS}</span>
</div>

<style>
	.title-input {
		font-size: 1.5em;
		font-weight: bold;
		margin: 0em;
		width: calc(100% - 0.5em);
	}

	.title-input[contenteditable]:empty::before {
		content: 'Enter survey title...';
		color: var(--text-dark-color);
	}

	.input-container {
		margin-bottom: -1.2em;
	}

	.char-count {
		left: 88%;
		font-size: 0.7em;
	}

	@media screen and (max-width: 768px) {
		.title-input {
			font-size: 1.25em;
		}

		.char-count {
			left: 72%;
			font-size: 0.6em;
		}
	}
</style>
