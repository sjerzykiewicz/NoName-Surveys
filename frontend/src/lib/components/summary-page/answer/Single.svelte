<script lang="ts">
	export let data: { answer: string; choices: string[] };
</script>

<div class="choice-area display">
	{#each data.choices as choice}
		<label title={choice === data.answer ? 'Selected answer' : 'Other choice'} class="choice">
			<div class="radio" class:selected={choice === data.answer}>
				<input type="radio" checked={choice === data.answer} disabled />
			</div>
			<div class="choice-input display" class:selected={choice === data.answer}>
				{choice}
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
		background-color: var(--primary-dark-color);
		cursor: default;
	}

	.choice-input.selected,
	.choice-input.selected:hover {
		background-color: var(--secondary-dark-color);
	}

	input {
		cursor: default;
	}
</style>
