<script lang="ts">
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	import Tx from 'sveltekit-translate/translate/tx.svelte';
	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let data: { answers: number[] };

	let existingAnswers = data.answers.filter((x) => x !== null);
</script>

{#if existingAnswers.length === 0}
	<div title={$t('no_answers_to_question')} class="summary_no_answers">
		<Tx text="no_answers_to_question" />
	</div>
{:else}
	<div class="choice-area display scale">
		{#each [1, 2, 3, 4, 5] as choice}
			<label title={$t('choice')} class="choice scale">
				<input type="radio" disabled />
				<div class="choice-input display scale">
					{choice}
				</div>
				<div class="choice-percentage" title={$t('average')}>
					{(
						(data.answers.filter((answer) => answer === choice).length / data.answers.length) *
						100
					).toFixed(2)}%
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

	input[type='radio'] {
		cursor: default;
	}

	.choice-percentage {
		margin-left: 0em;
		margin-top: 0.5em;
	}

	@media screen and (max-width: 768px) {
		.choice-area {
			width: 100%;
			margin-left: 0em;
		}

		.choice {
			padding: 0em;
		}
	}
</style>
