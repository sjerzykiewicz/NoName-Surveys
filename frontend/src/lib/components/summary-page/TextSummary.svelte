<script lang="ts">
	import { page } from '$app/stores';

	export let data: { answers: string[]; details: string };
</script>

<div class="choice-area display">
	{#if data.details}
		<div title="Question details" class="details">
			{data.details}
		</div>
	{/if}
	<div class="text-answers">
		{#each data.answers as answer, i}
			<a href="{$page.url.pathname}/{i}" title="Click to get all answers" class="text-area display">
				{answer}
			</a>
		{/each}
	</div>
</div>

<style>
	.text-answers {
		overflow-y: auto;
		max-height: 15em;
		background-color: var(--secondary-dark-color);
		margin-left: 2.25em;
		padding: 0.5em;
		border-radius: 5px;
		border: 1px solid var(--border-color);
		box-shadow: 0px 4px 4px var(--shadow-color);
	}

	.text-area {
		display: block;
		padding: 0.25em;
		margin-left: 0em;
		margin-bottom: 0.5em;
		cursor: pointer;
		text-decoration: none;
	}

	.text-area:hover {
		background-color: var(--secondary-color);
	}

	.text-area:last-of-type {
		margin-bottom: 0em;
	}

	.text-answers::-webkit-scrollbar {
		width: 0.8em;
	}

	.text-answers::-webkit-scrollbar-track {
		background-color: var(--secondary-dark-color);
		border-radius: 5px;
	}

	.text-answers::-webkit-scrollbar-thumb {
		background-color: var(--primary-color);
		background-clip: padding-box;
		border-radius: 5px;
		border: 2px solid var(--secondary-dark-color);
	}

	.text-answers::-webkit-scrollbar-thumb:hover {
		background-color: var(--text-dark-color);
	}

	.text-answers::-webkit-scrollbar-thumb:active {
		background-color: var(--border-color);
	}
</style>
