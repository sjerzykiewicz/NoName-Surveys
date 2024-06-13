<script lang="ts">
	export let data: { answer: string; choices: string[] };
</script>

<div class="choice-area display">
	{#each data.choices as choice}
		<div title={choice === data.answer ? 'Selected answer' : 'Other choice'} class="choice">
			<div class="choice-input display" class:selected={choice === data.answer}>
				{choice}
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

	.choice-input.selected,
	.choice-input.selected:hover {
		background-color: var(--secondary-dark-color);
	}
</style>
