<script lang="ts">
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	import Tx from 'sveltekit-translate/translate/tx.svelte';
	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);
	export let data: { multi_answers: string[][]; choices: string[] };
	const existingAnswers = data.multi_answers.filter((x) => x.length !== 0);
	function calculateAvgRank(choice: string): number {
		const totalAnswers = existingAnswers.length;
		const rankSum = existingAnswers
			.map((answers) => answers.indexOf(choice) + 1)
			.reduce((acc, curr) => acc + curr, 0);
		const avgRank = rankSum / totalAnswers;
		return parseFloat(avgRank.toFixed(2));
	}

	let rankedChoices: { choice: string; avgRank: number }[] = [];
	data.choices.forEach((c) => {
		rankedChoices.push({ choice: c, avgRank: calculateAvgRank(c) });
	});
	rankedChoices.sort((a, b) => a.avgRank - b.avgRank);
</script>

{#if existingAnswers.length === 0}
	<div title={$t('no_answers_to_question')} class="summary-no-answers">
		<Tx text="no_answers_to_question" />
	</div>
{:else}
	<div title={$t('ordered_by_average_place')} class="choice-area display">
		{#each rankedChoices as choice, answerIndex}
			<div class="choice">
				<div class="rank">{answerIndex + 1}.</div>
				<div class="choice-input display">
					{choice.choice}
				</div>
				<div class="choice-percentage" title={$t('average')}>
					<Tx text="average_choice_ranking" />: {choice.avgRank}
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
