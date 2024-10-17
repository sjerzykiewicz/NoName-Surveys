<script lang="ts">
	export let data: { answers: number[] };
</script>

<div class="choice-area display scale">
	{#each [1, 2, 3, 4, 5] as choice}
		<label title="Choice" class="choice scale">
			<input type="radio" disabled />
			<div class="choice-input display scale">
				{choice}
			</div>
			<div class="choice-percentage" title="Average">
				{(
					(data.answers.filter((answer) => answer === choice).length / data.answers.length) *
					100
				).toFixed(2)}%
			</div>
		</label>
	{/each}
</div>

<style>
	.choice-input,
	.choice-input:hover {
		background-color: var(--primary-dark-color);
		cursor: default;
	}

	input[type='radio'] {
		cursor: default;
	}

	.choice-percentage {
		margin-left: 0em;
		margin-top: 0.5em;
	}

	@media screen and (max-width: 768px) {
		.choice-area {
			width: 100%;
			margin-left: 0em;
		}

		.choice {
			padding: 0em;
		}
	}
</style>
