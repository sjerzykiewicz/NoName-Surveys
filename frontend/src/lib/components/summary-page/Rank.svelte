<script lang="ts">
	export let data: { answer: string[] };
</script>

<div class="choice-area">
	{#each data.answer as answer, answerIndex}
		<div title="Answer" class="choice">
			<div class="rank">{answerIndex + 1}.</div>
			<div class="choice-in">
				{answer}
			</div>
		</div>
	{/each}
</div>

<style>
	.choice {
		width: fit-content;
	}

	.choice-in {
		border: 2px solid var(--accent-color);
		background-color: var(--secondary-dark-color);
		font-weight: bold;
		color: var(--accent-color);
		cursor: default;
	}

	.choice-in:hover {
		background-color: var(--secondary-dark-color);
	}

	.rank {
		margin-right: 0.25em;
		font-size: 1.25em;
		font-weight: bold;
		color: var(--accent-color);
		cursor: default;
		width: 1.5em;
		text-align: right;
	}

	@media screen and (max-width: 767px) {
		.choice-in,
		.rank {
			font-size: 1em;
		}

		.rank {
			width: 2em;
		}
	}
</style>
