<script lang="ts">
	export let data: { answers: string[]; choices: string[] };

	function calculatePercentage(answer: string, answers: string[]) {
		return ((answers.filter((a) => a === answer).length / answers.length) * 100).toFixed(2);
	}
</script>

<div class="choice-area display">
	{#each data.choices as choice}
		<div class="choice">
			<div title="Choice" class="choice-input display">
				{choice}
			</div>
			<div title="Average" class="choice-percentage">
				{calculatePercentage(choice, data.answers)}%
			</div>
		</div>
	{/each}
</div>

<style>
	.choice-area {
		margin-left: 2.25em;
		width: calc(100% - 4.5em);
	}

	.choice-input,
	.choice-input:hover {
		background-color: var(--primary-dark-color);
		cursor: default;
	}
</style>
