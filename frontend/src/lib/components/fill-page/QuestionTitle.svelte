<script lang="ts">
	import { questions } from '$lib/stores/fill-page';

	export let questionIndex: number;
</script>

<div class="question-area">
	<div class="index">{questionIndex + 1}.</div>
	<div title="Question title" class="question-title">
		{$questions[questionIndex].question}
		{#if $questions[questionIndex].required}
			<span class="required">*</span>
		{/if}
	</div>
</div>

<style>
	.question-area {
		display: flex;
		flex-flow: row;
		align-items: flex-start;
		margin-bottom: 1em;
		font-size: 1.25em;
		font-weight: bold;
		color: var(--text-color);
		cursor: default;
	}

	.question-title {
		flex: 1;
		text-shadow: 0px 4px 4px var(--shadow-color);
		overflow: hidden;
	}

	.index {
		width: 1.4em;
		text-align: right;
		padding-right: 0.5em;
	}

	.required {
		color: var(--accent-color);
	}

	@media screen and (max-width: 767px) {
		.question-area,
		.index {
			font-size: 1em;
		}

		.index {
			width: 2em;
		}
	}
</style>
