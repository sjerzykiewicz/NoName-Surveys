<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';

	export let questionIndex: number;
	$answers[questionIndex].choices[0] = '';
</script>

<div class="choice-area">
	<div title="Question details" class="details">
		{$questions[questionIndex].choices[0]}
	</div>
	<div
		title="Enter your answer"
		class="text-area"
		contenteditable
		bind:textContent={$answers[questionIndex].choices[0]}
	>
		{$answers[questionIndex].choices[0]}
	</div>
</div>

<style>
	.choice-area {
		padding-left: 2.3em;
	}

	.text-area {
		font-size: 1.25em;
		min-height: 6em;
	}

	.text-area[contenteditable]:empty::before {
		content: 'Enter your answer...';
	}

	@media screen and (max-width: 767px) {
		.choice-area,
		.details,
		.text-area {
			font-size: 1em;
		}
	}
</style>
