<script lang="ts">
	export let data: { multi_answers: string[]; choices: string[] };

	function calculatePercentage(choice: string) {
		const count = data.multi_answers.filter((answer) => answer.includes(choice)).length;
		const percentage = (count / data.multi_answers.length) * 100;
		return percentage.toFixed(2) + '%';
	}
</script>

<div class="choice-area">
	{#each data.choices as choice}
		<label class="choice">
			<div class="radio">
				<input type="checkbox" disabled />
			</div>
			<div class="choice-in">
				{choice}
			</div>
			<div class="choice-percentage" title="Average">
				{calculatePercentage(choice)}
			</div>
		</label>
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
		cursor: default;
	}

	@media screen and (max-width: 767px) {
		.choice-area,
		.choice-in {
			font-size: 1em;
		}
	}
</style>
