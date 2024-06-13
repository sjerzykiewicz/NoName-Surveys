<script lang="ts">
	export let data: { answer: string[]; choices: string[] };
</script>

<div class="choice-area display">
	{#each data.choices as choice}
		<label title={data.answer.includes(choice) ? 'Selected answer' : 'Other choice'} class="choice">
			<div class="checkbox" class:selected={data.answer.includes(choice)}>
				<input type="checkbox" checked={data.answer.includes(choice)} disabled />
			</div>
			<div class="choice-input display" class:selected={data.answer.includes(choice)}>
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
