<script lang="ts">
	import { title } from '$lib/stores/create-page';
	import TitleError from './TitleError.svelte';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	export let titleError: boolean;
</script>

<div
	title="Enter survey title"
	class="title-input"
	contenteditable
	bind:textContent={$title}
	in:slide={{ duration: 200, easing: cubicInOut }}
>
	{$title}
</div>
<TitleError {titleError} />

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
