<script lang="ts">
	export let data: { multi_answers: string[]; choices: string[] };

	function calculatePercentage(choice: string) {
		const count = data.multi_answers.filter((answer) => answer.includes(choice)).length;
		const percentage = (count / data.multi_answers.length) * 100;
		return percentage.toFixed(2) + '%';
	}
</script>

<div class="choice-area display">
	{#each data.choices as choice}
		<label title="Choice" class="choice">
			<div class="checkbox">
				<input type="checkbox" disabled />
			</div>
			<div class="choice-input display">
				{choice}
			</div>
			<div title="Average" class="choice-percentage">
				{calculatePercentage(choice)}
			</div>
		</label>
	{/each}
</div>

<style>
	.choice {
		cursor: default;
	}

	.choice-input,
	.choice-input:hover {
		background-color: var(--primary-color-2);
		cursor: default;
		transition:
			0.2s,
			outline 0s;
	}

	input {
		cursor: default !important;
	}
</style>
