<script lang="ts">
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);
	export let data: { answers: string[][]; choices: string[] };

	function calculateAvgPlace(choice: string) {
		const totalAnswers = data.answers.length;
		const choiceCount = data.answers
			.map((answers) => answers.indexOf(choice))
			.reduce((acc, curr) => acc + curr, 0);
		const avgPlace = choiceCount / totalAnswers;
		return avgPlace.toFixed(2);
	}
</script>

<div title={$t('ordered_by_average_place')} class="choice-area display">
	{#each data.choices.sort((a, b) => parseFloat(calculateAvgPlace(a)) - parseFloat(calculateAvgPlace(b))) as choice, answerIndex}
		<div class="choice">
			<div class="rank">{answerIndex + 1}.</div>
			<div class="choice-input display">
				{choice}
			</div>
		</div>
	{/each}
</div>

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
