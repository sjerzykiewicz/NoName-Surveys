<script lang="ts">
	export let data: { answer: number };
</script>

<div class="choice-area display scale">
	{#each [1, 2, 3, 4, 5] as choice}
		<label title={choice === data.answer ? 'Selected answer' : 'Other choice'} class="choice scale">
			<input type="radio" checked={choice === data.answer} disabled />
			<div class="choice-input display scale" class:selected={choice === data.answer}>
				{choice}
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

	.choice-input.selected {
		background-color: var(--secondary-dark-color);
	}

	input[type='radio'] {
		cursor: default;
	}
</style>
