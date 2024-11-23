<script lang="ts">
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	import Tx from 'sveltekit-translate/translate/tx.svelte';
	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);
	export let data: { answer: number };
</script>

{#if data.answer === null}
	<div title={$t('question_not_answered')} class="summary-no-answers">
		<Tx text="question_not_answered" />
	</div>
{:else}
	<div class="choice-area display scale">
		{#each [1, 2, 3, 4, 5] as choice}
			<label
				title={choice === data.answer ? $t('selected_answer') : $t('other_choice')}
				class="choice scale"
			>
				<input type="radio" checked={choice === data.answer} disabled />
				<div class="choice-input display scale" class:selected={choice === data.answer}>
					{choice}
				</div>
			</label>
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

	.choice-input.selected {
		background-color: var(--secondary-color-2);
	}

	input[type='radio'] {
		cursor: default;
	}
</style>
