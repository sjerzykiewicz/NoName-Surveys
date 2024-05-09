<script lang="ts">
	export let data: { answer: string; choices: string[] };
</script>

<div class="choice-area">
	{#each data.choices as choice}
		<label title={choice === data.answer ? 'Answer' : ''} class="choice">
			<div class="radio" class:selected={choice === data.answer}>
				<input type="radio" checked={choice === data.answer} disabled />
			</div>
			<div class="choice-in" class:selected={choice === data.answer}>
				{choice}
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
		border-radius: 50%;
	}

	input {
		margin: 0em;
		cursor: default;
	}

	@media screen and (max-width: 767px) {
		.choice-area,
		.choice-in {
			font-size: 1em;
		}
	}
</style>
