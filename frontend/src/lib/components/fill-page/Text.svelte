<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';

	export let questionIndex: number;
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

	.details {
		font-size: 1.25em;
		margin-top: -0.5em;
		margin-bottom: 0.5em;
		text-shadow: 0px 4px 4px var(--box-shadow-color);
		cursor: default;
	}

	.text-area {
		font-size: 1.25em;
		background-color: var(--secondary-color);
		padding: 0.5em;
		border: 1px solid var(--border-color);
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--box-shadow-color);
		cursor: text;
		color: var(--text-color);
		min-height: 6em;
	}

	.text-area[contenteditable]:empty::before {
		content: 'Enter your answer...';
		color: var(--text-color-transparent);
	}

	@media screen and (max-width: 767px) {
		.choice-area,
		.details,
		.text-area {
			font-size: 1em;
		}
	}
</style>
