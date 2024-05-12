<script lang="ts">
	export let data: { answers: number[] };
</script>

<div class="choice-area">
	{#each [1, 2, 3, 4, 5] as choice}
		<label title="Answer" class="choice">
			<div class="scale">
				<input type="radio" disabled />
			</div>
			<div class="number">
				{choice}
			</div>
			<div class="choice-percentage">
				{(
					(data.answers.filter((answer) => answer === choice).length / data.answers.length) *
					100
				).toFixed(2)}%
			</div>
		</label>
	{/each}
</div>

<style>
	.choice-area {
		display: flex;
		flex-flow: row;
		align-items: center;
		justify-content: space-around;
		width: calc(86% - 2.25em);
		margin-left: 2.25em;
	}

	.choice {
		flex-flow: column;
		padding: 0.5em;
		margin-bottom: 0em;
		cursor: default;
	}

	.number {
		font-size: 1.25em;
		margin-top: 0.25em;
		text-shadow: 0px 4px 4px var(--shadow-color);
	}

	input[type='radio'] {
		margin: 0em;
		cursor: default;
	}

	.choice-percentage {
		margin-left: none;
		margin-top: 0.5em;
	}

	@media screen and (max-width: 767px) {
		.choice-area,
		.number {
			font-size: 1em;
		}
	}
</style>
