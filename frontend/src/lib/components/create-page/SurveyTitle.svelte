<script lang="ts">
	import { title } from '$lib/stores/create-page';
	import { handleNewLine } from '$lib/utils/handleNewLine';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	let innerWidth: number;
</script>

<svelte:window bind:innerWidth />

<!-- svelte-ignore a11y-autofocus -->
<div
	title="Enter survey title"
	class="title-input"
	id="title"
	contenteditable
	bind:textContent={$title}
	autofocus={innerWidth > 767}
	role="textbox"
	tabindex="0"
	on:keydown={handleNewLine}
	in:slide={{ delay: 200, duration: 200, easing: cubicInOut }}
	out:slide={{ duration: 200, easing: cubicInOut }}
>
	{$title}
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

	@media screen and (max-width: 767px) {
		.title-input {
			font-size: 1.25em;
		}
	}
</style>
