<script lang="ts">
	export let data: { answer: number };
</script>

<div class="choice-area">
	{#each [1, 2, 3, 4, 5] as choice}
		<label title={choice === data.answer ? 'Answer' : ''} class="choice">
			<input type="radio" checked={choice === data.answer} disabled />
			<div class="number" class:selected={choice === data.answer}>
				{choice}
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
		cursor: pointer;
	}

	.number {
		font-size: 1.25em;
		margin-top: 0.25em;
		text-shadow: 0px 4px 4px var(--shadow-color);
	}

	.number.selected {
		font-weight: bold;
		color: var(--accent-color);
	}

	input[type='radio'] {
		margin: 0em;
	}

	@media screen and (max-width: 767px) {
		.choice-area,
		.number {
			font-size: 1em;
		}
	}
</style>
