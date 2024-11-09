<script lang="ts">
	import { LIMIT_OF_CHARS } from '$lib/stores/global';

	export let text: string;
	export let label: string;
	export let title: string;
	export let id: string = '';
	export let element: HTMLDivElement | null = null;
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

	function trimBr() {
		if (text.length === 0 && element) element.innerHTML = '';
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
		on:keydown|once={() => (text = '')}
		on:keydown={(e) => {
			handleEnter(e);
			limitInput(e);
		}}
		on:keyup={trimBr}
		on:paste={handlePaste}
		on:drop={handleDrop}
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
		overflow: hidden;
		white-space: pre-wrap !important;
		pointer-events: all;
		transition:
			0.2s,
			outline 0s;
	}

	.input-container {
		flex: var(--container-flex, 1);
		margin-top: var(--container-margin, -1.1em);
		margin-bottom: var(--container-margin, -1.1em);

		width: 100%;
		overflow: hidden;
		padding: 0.2em;
		margin-left: -0.2em;
		margin-right: -0.2em;
		pointer-events: none;
	}

	.input-label,
	.char-count {
		font-size: var(--font-size, 0.6em);

		position: relative;
		color: var(--text-color-1);
		background-color: var(--secondary-color-2);
		border-radius: 5px;
		padding: 0em 0.3em;
		width: fit-content;
		text-align: center;
		cursor: default;
		z-index: 1;
		transition:
			color 0.2s,
			background-color 0.2s;
	}

	.input-label {
		left: var(--label-left, 0.5em);
		top: var(--label-top, 8px);
	}

	.char-count {
		left: var(--count-left, calc(100% - 8em));
		bottom: var(--count-bottom, 6px);
	}

	.input-container .input:focus + .char-count {
		visibility: visible;
	}

	.char-count.max {
		color: var(--error-color-1);
		border-color: var(--error-color-1);
		visibility: visible;
	}

	#title {
		font-size: 1.2em;
		font-weight: 700 !important;
		width: calc(100% - 0.5em);
	}

	@media screen and (max-width: 768px) {
		.input-label {
			top: var(--label-top-mobile, 6px);
		}

		.char-count {
			bottom: var(--count-bottom-mobile, 4px);
		}

		#title {
			font-size: 1.25em;
		}
	}
</style>
