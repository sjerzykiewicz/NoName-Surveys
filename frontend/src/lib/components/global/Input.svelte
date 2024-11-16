<script lang="ts">
	import { LIMIT_OF_CHARS } from '$lib/stores/global';

	export let text: string;
	export let label: string;
	export let title: string;
	export let id: string = '';
	export let element: HTMLDivElement | null = null;
	export let clearOnce: boolean = false;
	export let handleEnter: (e: KeyboardEvent) => void = (e) => handleNewLine(e);

	const keys = [
		'ArrowDown',
		'ArrowLeft',
		'ArrowRight',
		'ArrowUp',
		'End',
		'Home',
		'PageDown',
		'PageUp',
		'Backspace',
		'Delete'
	];

	function limitInput(e: KeyboardEvent) {
		if (text.length >= $LIMIT_OF_CHARS && !keys.includes(e.key)) {
			e.preventDefault();
		}
	}

	function handleNewLine(e: KeyboardEvent) {
		if (e.key === 'Enter') {
			e.preventDefault();
			document.execCommand('insertLineBreak');
		}
	}

	function handlePaste(e: ClipboardEvent) {
		e.preventDefault();
		const text = e.clipboardData ? e.clipboardData.getData('text/plain') : '';
		document.execCommand('insertText', false, text);
	}

	function handleDrop(e: DragEvent) {
		e.preventDefault();
		const text = e.dataTransfer ? e.dataTransfer.getData('text/plain') : '';
		document.execCommand('insertText', false, text);
	}

	function trimBr(elem: HTMLDivElement) {
		if (text.length === 0) elem.innerHTML = '';
	}
</script>

<div class="input-container">
	<div class="input-label">{label}</div>
	<div
		{title}
		{id}
		class="input"
		placeholder={title + '...'}
		contenteditable
		role="textbox"
		tabindex="0"
		bind:textContent={text}
		bind:this={element}
		on:keydown|once={() => {
			if (clearOnce) text = '';
		}}
		on:keydown={(e) => {
			handleEnter(e);
			limitInput(e);
		}}
		on:paste={handlePaste}
		on:drop={handleDrop}
		on:keyup={(e) => trimBr(e.currentTarget)}
	></div>
	<div class="char-count" class:max={text.length > $LIMIT_OF_CHARS}>
		{text.length} / {$LIMIT_OF_CHARS}
	</div>
</div>

<style>
	.input:empty::before {
		content: attr(placeholder);
		color: var(--text-color-3) !important;
	}

	.input {
		margin-right: var(--margin-right, 0.5em);

		flex: 1;
		background-color: var(--secondary-color-2);
		padding: 0.25em;
		border: 1px solid var(--border-color-1);
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--shadow-color-1);
		color: var(--text-color-1);
		cursor: text;
		overflow-x: hidden;
		overflow-y: auto;
		overflow-wrap: break-word;
		max-height: 5.75em;
		white-space: pre-wrap !important;
		pointer-events: all;
		transition:
			0.2s,
			outline 0s;
	}

	.input-container {
		flex: 1;
		width: 100%;
		overflow: hidden;
		padding: 0.2em;
		margin: var(--container-margin, -1em) -0.2em;
		pointer-events: none;
	}

	.input-label,
	.char-count {
		position: relative;
		color: var(--text-color-1);
		background-color: var(--secondary-color-2);
		border-radius: 5px;
		padding: 0em 0.3em;
		width: fit-content;
		font-size: 0.6em;
		text-align: center;
		cursor: default;
		z-index: 1;
		transition:
			color 0.2s,
			background-color 0.2s;
	}

	.input-label {
		left: 0.5em;
		top: var(--label-top, 8px);
	}

	.char-count {
		left: calc(100% - var(--char-count-left, 8em));
		bottom: 6px;
		visibility: hidden;
	}

	.input:focus + .char-count {
		visibility: visible;
	}

	.char-count.max {
		color: var(--error-color-1);
		border-color: var(--error-color-1);
		visibility: visible;
	}

	@media screen and (max-width: 768px) {
		.input-label {
			top: var(--label-top-mobile, 6px);
		}

		.char-count {
			bottom: 4px;
		}
	}
</style>
