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
		max-height: 15em;
		background-color: var(--secondary-color-2);
		margin-left: 2.25em;
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
		min-height: 1.15em;
		transition:
			0.2s,
			outline 0s;
	}

	.text-input:hover {
		background-color: var(--secondary-color-1);
	}

	.text-input:last-of-type {
		margin-bottom: 0em;
	}

	.text-answers::-webkit-scrollbar {
		width: 0.8em;
	}

	.text-answers::-webkit-scrollbar-track {
		background-color: var(--secondary-color-2);
		border-radius: 5px;
	}

	.text-answers::-webkit-scrollbar-thumb {
		background-color: var(--primary-color-1);
		background-clip: padding-box;
		border-radius: 5px;
		border: 2px solid var(--secondary-color-2);
		transition:
			0.2s,
			outline 0s;
	}

	.text-answers::-webkit-scrollbar-thumb:hover {
		background-color: var(--text-color-3);
	}

	.text-answers::-webkit-scrollbar-thumb:active {
		background-color: var(--border-color-1);
	}
</style>
