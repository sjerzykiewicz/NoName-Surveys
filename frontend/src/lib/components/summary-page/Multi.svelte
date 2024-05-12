<script lang="ts">
	export let data: { answer: string[]; choices: string[] };
</script>

<div class="choice-area">
	{#each data.choices as choice}
		<label title={data.answer.includes(choice) ? 'Answer' : ''} class="choice">
			<div class="radio" class:selected={data.answer.includes(choice)}>
				<input type="checkbox" checked={data.answer.includes(choice)} disabled />
			</div>
			<div class="choice-in" class:selected={data.answer.includes(choice)}>
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
		border-radius: 3px;
		background-color: var(--accent-color);
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
