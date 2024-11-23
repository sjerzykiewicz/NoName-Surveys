<script lang="ts">
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	import Tx from 'sveltekit-translate/translate/tx.svelte';
	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let data: { answer: string; details: string };
</script>

{#if data.answer === ''}
	<div title={$t('question_not_answered')} class="summary_no_answers">
		<Tx text="question_not_answered" />
	</div>
{:else}
	<div class="choice-area text display">
		<div title={$t('question_details')} class="details">
			{data.details}
		</div>
		<div title={$t('answer')} class="text-input display">
			{data.answer}
		</div>
	</div>
{/if}

<style>
	.text-input {
		border: 1px solid var(--accent-color-1);
		background-color: var(--secondary-color-2);
		color: var(--accent-color-1);
		transition:
			0.2s,
			outline 0s;
	}
</style>
