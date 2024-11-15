<script lang="ts">
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let data: { answers: string[]; choices: string[] };

	function calculatePercentage(answer: string, answers: string[]) {
		return ((answers.filter((a) => a === answer).length / answers.length) * 100).toFixed(2);
	}
</script>

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
				{calculatePercentage(choice, data.answers)}%
			</div>
		</div>
	{/each}
</div>

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
