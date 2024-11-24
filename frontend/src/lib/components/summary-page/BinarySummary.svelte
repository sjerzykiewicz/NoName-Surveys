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
	<div title={$t('no_answers_to_question')} class="summary_no_answers">
		<Tx text="no_answers_to_question" />
	</div>
{:else}
	<div class="choice-area display binary">
		<label title={$t('choice')} class="choice binary">
			<div class="icon">
				<input type="radio" disabled />
				<i class="symbol">thumb_up</i>
			</div>
			<div class="choice-input display binary">
				{data.choices[0]}
			</div>
			<div class="choice-percentage" title={$t('average')}>
				{calculatePercentage(data.choices[0], existingAnswers)}%
			</div>
		</label>
		<label title={$t('choice')} class="choice binary">
			<div class="icon">
				<input type="radio" disabled />
				<i class="symbol">thumb_down</i>
			</div>
			<div class="choice-input display binary">
				{data.choices[1]}
			</div>
			<div class="choice-percentage" title={$t('average')}>
				{calculatePercentage(data.choices[1], existingAnswers)}%
			</div>
		</label>
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

	.choice-input {
		margin-top: 0.5em;
	}

	input {
		cursor: default !important;
	}

	i {
		font-size: 1.25em;
	}

	.choice-percentage {
		margin-left: 0em;
		margin-top: 0.5em;
	}

	@media screen and (max-width: 768px) {
		.choice-percentage {
			margin-left: 0.5em;
			margin-top: 0em;
		}

		.choice-input {
			margin-top: 0em;
		}
	}
</style>
