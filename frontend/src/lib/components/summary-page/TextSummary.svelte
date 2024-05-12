<script lang="ts">
	import { page } from '$app/stores';

	export let data: { answers: string[]; details: string };
</script>

<div class="choice-area">
	{#if data.details}
		<div title="Details" class="details">
			{data.details}
		</div>
	{/if}
	<div class="text-answers">
		{#each data.answers as answer, i}
			<a href="{$page.url.pathname}/{i}" title="Answers" class="text-area">
				{answer}
			</a>
		{/each}
	</div>
</div>

<style>
	.choice-area {
		padding-left: 2.3em;
	}

	.details {
		font-size: 1.25em;
		margin-top: -0.5em;
		margin-bottom: 0.5em;
		text-shadow: 0px 4px 4px var(--shadow-color);
		cursor: default;
	}
	.text-answers {
		overflow-y: auto;
		overflow-x: hidden;
		max-height: 200px;
		width: 100%;
		background-color: var(--secondary-dark-color);
		padding: 1em;
		border-radius: 5px;
		border: 2px solid var(--accent-color);
		box-shadow: 0px 4px 4px var(--shadow-color);
	}

	.text-area {
		display: block;
		background-color: var(--secondary-color);
		padding: 0.25em;
		margin-bottom: 0.5em;
		border: 2px solid var(--primary-color);
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--shadow-color);
		font-size: 1.25em;
		font-weight: bold;
		width: fit-content;
		max-width: 100%;
		overflow: hidden;
		overflow-wrap: break-word;
		margin-right: 0.5em;
		cursor: pointer;
		text-decoration: none;
		color: var(--text-color);
	}

	@media screen and (max-width: 767px) {
		.choice-area,
		.details,
		.text-area {
			font-size: 1em;
		}
	}
</style>
