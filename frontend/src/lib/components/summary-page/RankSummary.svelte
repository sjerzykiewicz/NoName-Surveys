<script lang="ts">
	export let data: { answers: string[][]; choices: string[] };

	function calculateAvgPlace(choice: string) {
		const totalAnswers = data.answers.length;
		const choiceCount = data.answers
			.map((answers) => answers.indexOf(choice))
			.reduce((acc, curr) => acc + curr, 0);
		const avgPlace = choiceCount / totalAnswers;
		return avgPlace.toFixed(2);
	}
</script>

<div class="choice-area" title="Ordered by average place">
	{#each data.choices.sort((a, b) => parseFloat(calculateAvgPlace(a)) - parseFloat(calculateAvgPlace(b))) as choice, answerIndex}
		<div class="choice">
			<div class="rank">{answerIndex + 1}.</div>
			<div class="choice-in">
				{choice}
			</div>
		</div>
	{/each}
</div>

<style>
	.choice {
		width: fit-content;
	}

	.choice-in {
		font-weight: bold;
		cursor: default;
	}

	.choice-in:hover {
		background-color: var(--primary-color);
	}

	.rank {
		margin-right: 0.25em;
		font-size: 1.25em;
		font-weight: bold;
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
