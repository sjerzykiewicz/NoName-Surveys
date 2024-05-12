<script lang="ts">
	export let data: { answers: string[][]; choices: string[] };

	function calculatePercentage(choice: string) {
		const totalAnswers = data.answers.flat().length;
		const choiceCount = data.answers.flat().filter((answers) => answers === choice).length;
		const percentage = (choiceCount / totalAnswers) * 100;
		return `${percentage.toFixed(2)}%`;
	}
</script>

<div class="choice-area">
	{#each data.choices as choice}
		<label title={data.answers.includes([choice]) ? 'Answer' : ''} class="choice">
			<div class="radio" class:selected={data.answers.includes([choice])}>
				<input type="checkbox" checked={data.answers.includes([choice])} disabled />
			</div>
			<div class="choice-in" class:selected={data.answers.includes([choice])}>
				{choice}
			</div>
			<div class="choice-percentage">
				{calculatePercentage(choice)}
			</div>
		</label>
	{/each}
</div>

<style>
	.choice {
		width: fit-content;
		cursor: default;
	}

	.choice-in {
		cursor: default;
	}

	.choice-in:hover {
		background-color: var(--primary-color);
	}

	.choice-in.selected {
		background-color: var(--secondary-dark-color);
	}

	.radio.selected {
		display: flex;
		align-items: center;
		justify-content: center;
		margin-left: 0.75em;
		height: 11px;
		width: 11px;
		border: 4px solid var(--accent-color);
		border-radius: 3px;
	}

	input {
		cursor: default;
	}

	@media screen and (max-width: 767px) {
		.choice-area,
		.choice-in {
			font-size: 1em;
		}
	}
</style>
