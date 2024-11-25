<script lang="ts">
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	import Tx from 'sveltekit-translate/translate/tx.svelte';
	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let data: { answers: string[]; choices: string[] };

	let existingAnswers = data.answers.filter((x) => x !== null);

	function calculatePercentage(answer: string, answers: string[]) {
		return ((answers.filter((a) => a === answer).length / answers.length) * 100).toFixed(2);
	}
</script>

{#if existingAnswers.length === 0}
	<div title={$t('no_answers_to_question')} class="summary-no-answers">
		<Tx text="no_answers_to_question" />
	</div>
{:else}
	<div class="choice-area display">
		{#each data.choices as choice}
			<div title={$t('choice')} class="choice">
				<div class="radio">
					<input type="radio" disabled />
				</div>
				<div class="choice-input display">
					{choice}
				</div>
				<div title={$t('average')} class="choice-percentage">
					{calculatePercentage(choice, existingAnswers)}%
				</div>
			</div>
		{/each}
	</div>
{/if}

<style>
	.choice {
		cursor: default;
	}

	.choice-input,
	.choice-input:hover {
		background-color: var(--primary-color-2);
		cursor: default;
		transition:
			0.2s,
			outline 0s;
	}

	input {
		cursor: default !important;
	}
</style>
