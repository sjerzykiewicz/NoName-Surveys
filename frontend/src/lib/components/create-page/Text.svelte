<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { handleNewLine } from '$lib/utils/handleNewLine';

	export let questionIndex: number;
</script>

<div
	class="choice-area"
	in:slide={{ delay: 200, duration: 200, easing: cubicInOut }}
	out:slide={{ duration: 200, easing: cubicInOut }}
>
	<div class="details">
		<div
			title="Enter question details"
			class="details-input"
			contenteditable
			bind:textContent={$questions[questionIndex].choices[0]}
			role="textbox"
			tabindex="0"
			on:keydown={handleNewLine}
		>
			{$questions[questionIndex].choices[0]}
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
</style>
