<script lang="ts">
	export let data: { answers: string[]; choices: string[] };

	function calculatePercentage(answer: string, answers: string[]) {
		return ((answers.filter((a) => a === answer).length / answers.length) * 100).toFixed(2);
	}
</script>

<div class="choice-area">
	{#each data.choices as choice}
		<div class="choice">
			<div class="radio">
				<input type="radio" disabled />
			</div>
			<div class="choice-in">
				{choice}
			</div>
			<div class="choice-percentage" title="Average">
				{calculatePercentage(choice, data.answers)}%
			</div>
		</div>
	{/each}
</div>

<style>
	.choice {
		cursor: default;
	}

	.choice-in {
		cursor: default;
	}

	.choice-in:hover {
		background-color: var(--primary-color);
	}

	input {
		margin: 0em;
		cursor: default;
	}

	@media screen and (max-width: 767px) {
		.choice-area,
		.choice-in {
			font-size: 1em;
		}
	}
</style>
