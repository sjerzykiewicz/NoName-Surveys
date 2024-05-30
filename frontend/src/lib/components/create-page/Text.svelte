<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { handleNewLine } from '$lib/utils/handleNewLine';

	export let questionIndex: number;
</script>

<div class="choice-area">
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
