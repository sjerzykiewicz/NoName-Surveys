<script lang="ts">
	export let data: { answer: string; choices: string[] };
</script>

<div class="choice-area">
	{#each data.choices as choice}
		<label title={choice === data.answer ? 'Answer' : ''} class="choice">
			<div class="radio">
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
		cursor: pointer;
	}

	@media screen and (max-width: 767px) {
		.choice-area,
		.choice-in {
			font-size: 1em;
		}
	}
</style>
