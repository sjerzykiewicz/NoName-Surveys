<script lang="ts">
	export let data: { answer: string; choices: string[] };
</script>

<div class="choice-area">
	<select title="Answer" value={data.answer} disabled>
		{#each data.choices as choice}
			<option value={choice}>
				{choice}
			</option>
		{/each}
	</select>
</div>

<style>
	.choice-area {
		padding-left: 2.3em;
	}

	select {
		background-color: var(--primary-color);
		padding: 0.25em;
		border: 1px solid var(--border-color);
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--shadow-color);
		font-size: 1.25em;
		cursor: pointer;
		font-weight: normal;
		color: var(--text-color);
		max-width: 100%;
		transition: 0.2s;
	}

	select:disabled {
		opacity: 1;
	}

	@media screen and (max-width: 767px) {
		select {
			font-size: 1em;
		}
	}
</style>
