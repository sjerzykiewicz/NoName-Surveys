<script lang="ts">
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	import Tx from 'sveltekit-translate/translate/tx.svelte';
	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);
	export let data: { answer: string; choices: string[] };
</script>

{#if data.answer === ''}
	<div title={$t('question_not_answered')} class="summary-no-answers">
		<Tx text="question_not_answered" />
	</div>
{:else}
	<div class="choice-area display">
		{#each data.choices as choice}
			<div
				title={choice === data.answer ? $t('selected_answer') : $t('other_choice')}
				class="choice"
			>
				<div class="choice-input display" class:selected={choice === data.answer}>
					{choice}
				</div>
			</div>
		{/each}
	</div>
{/if}

<style>
	.choice-area {
		margin-left: 2.25em;
		width: calc(100% - 4.5em);
	}

	.choice-input,
	.choice-input:hover {
		background-color: var(--primary-color-2);
		cursor: default;
		transition:
			0.2s,
			outline 0s;
	}

	.choice-input.selected,
	.choice-input.selected:hover {
		background-color: var(--secondary-color-2);
		transition:
			0.2s,
			outline 0s;
	}
</style>
