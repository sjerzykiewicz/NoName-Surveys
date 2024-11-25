<script lang="ts">
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	import Tx from 'sveltekit-translate/translate/tx.svelte';
	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);
	export let data: { answer: string[] };
</script>

{#if data.answer.length === 0}
	<div title={$t('question_not_answered')} class="summary-no-answers">
		<Tx text="question_not_answered" />
	</div>
{:else}
	<div class="choice-area display">
		{#each data.answer as answer, answerIndex}
			<div title={$t('answer_no', { index: answerIndex + 1 })} class="choice">
				<div class="rank">{answerIndex + 1}.</div>
				<div class="choice-input display">
					{answer}
				</div>
			</div>
		{/each}
	</div>
{/if}

<style>
	.choice-input,
	.choice-input:hover {
		background-color: var(--primary-color-2);
		cursor: default;
		transition:
			0.2s,
			outline 0s;
	}
</style>
