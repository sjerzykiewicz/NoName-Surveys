<script lang="ts">
	import { page } from '$app/stores';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	import Tx from 'sveltekit-translate/translate/tx.svelte';
	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);
	export let data: { answers: string[]; details: string };

	const existingData = data.answers.filter((x) => x !== '');
</script>

{#if existingData.length === 0}
	<div title={$t('no_answers_to_question')} class="summary_no_answers">
		<Tx text="no_answers_to_question" />
	</div>
{:else}
	<div class="choice-area text display">
		{#if data.details}
			<div title={$t('question_details')} class="details">
				{data.details}
			</div>
		{/if}
		<div class="text-answers">
			{#each data.answers as answer, i}
				{#if answer}
					{#if $page.url.pathname.includes('imported')}
						<div title={$t('selected_answer')} class="text-input display imported">
							{answer}
						</div>
					{:else}
						<a
							href="{$page.url.pathname}/answers/0/{i}"
							title={$t('click_to_get_answers')}
							class="text-input display"
						>
							{answer}
						</a>
					{/if}
				{/if}
			{/each}
		</div>
	</div>
{/if}

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

	.imported {
		background-color: var(--primary-color-2) !important;
		cursor: default !important;
	}
</style>
