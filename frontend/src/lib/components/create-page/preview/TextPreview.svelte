<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { handleNewLine } from '$lib/utils/handleNewLine';

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
		title="Enter your answer"
		class="text-area"
		contenteditable
		bind:textContent={$questions[questionIndex].choices[1]}
		role="textbox"
		tabindex="0"
		on:keydown={handleNewLine}
	>
		{$questions[questionIndex].choices[1]}
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
