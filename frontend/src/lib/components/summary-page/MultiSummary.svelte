<script lang="ts">
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	import Tx from 'sveltekit-translate/translate/tx.svelte';
	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let data: { multi_answers: string[]; choices: string[] };

	let existingAnswers = data.multi_answers.filter((x) => x.length !== 0);

	function calculatePercentage(choice: string) {
		const count = data.multi_answers.filter((answer) => answer.includes(choice)).length;
		const percentage = (count / data.multi_answers.length) * 100;
		return percentage.toFixed(2) + '%';
	}
</script>

{#if existingAnswers.length === 0}
	<div title={$t('no_answers_to_question')} class="summary_no_answers">
		<Tx text="no_answers_to_question" />
	</div>
{:else}
	<div class="choice-area display">
		{#each data.choices as choice}
			<label title={$t('choice')} class="choice">
				<div class="checkbox">
					<input type="checkbox" disabled />
				</div>
				<div class="choice-input display">
					{choice}
				</div>
				<div title={$t('average')} class="choice-percentage">
					{calculatePercentage(choice)}
				</div>
			</label>
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
