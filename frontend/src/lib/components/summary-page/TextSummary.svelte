<script lang="ts">
	import { page } from '$app/stores';

	export let data: { answers: string[]; details: string };
</script>

<div class="choice-area text display">
	{#if data.details}
		<div title="Question details" class="details">
			{data.details}
		</div>
	{/if}
	<div class="text-answers">
		{#each data.answers as answer, i}
			{#if answer}
				<a
					href="{$page.url.pathname}/answers/{i}"
					title="Click to get all answers"
					class="text-input display"
				>
					{answer}
				</a>
			{/if}
		{/each}
	</div>
</div>

<style>
	.text-answers {
		overflow-y: auto;
		min-height: 1.15em;
		max-height: 16.5em;
		background-color: var(--secondary-color-2);
		padding: 0.5em;
		border-radius: 5px;
		border: 1px solid var(--border-color-1);
		box-shadow: 0px 4px 4px var(--shadow-color-1);
	}

	.text-input {
		display: block;
		padding: 0.25em;
		margin-left: 0em;
		margin-bottom: 0.5em;
		cursor: pointer;
		text-decoration: none;
		transition:
			0.2s,
			outline 0s;
	}

	.text-input:hover {
		background-color: var(--secondary-color-1);
	}

	.text-input:active {
		background-color: var(--border-color-1);
	}

	.text-input:last-of-type {
		margin-bottom: 0em;
	}
</style>
