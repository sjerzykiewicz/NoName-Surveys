<script lang="ts">
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	import Tx from 'sveltekit-translate/translate/tx.svelte';
	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);
	export let data: { answer: string; choices: string[] };
</script>

{#if data.answer === null}
	<div title={$t('question_not_answered')} class="summary-no-answers">
		<Tx text="question_not_answered" />
	</div>
{:else}
	<div class="choice-area display binary">
		<label
			title={data.choices[0] === data.answer ? $t('selected_answer') : $t('other_choice')}
			class="choice binary"
			class:selected={data.choices[0] === data.answer}
		>
			<div class="icon">
				<input type="radio" disabled />
				<i class="symbol">thumb_up</i>
			</div>
			<div class="choice-input display binary">
				{data.choices[0]}
			</div>
		</label>
		<label
			title={data.choices[1] === data.answer ? $t('selected_answer') : $t('other_choice')}
			class="choice binary"
			class:selected={data.choices[1] === data.answer}
		>
			<div class="icon">
				<input type="radio" disabled />
				<i class="symbol">thumb_down</i>
			</div>
			<div class="choice-input display binary">
				{data.choices[1]}
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

	.selected .choice-input,
	.selected .choice-input:hover {
		background-color: var(--secondary-color-2);
		transition:
			0.2s,
			outline 0s;
	}

	input {
		cursor: default !important;
	}

	i {
		font-size: 1.25em;
	}

	.selected i {
		color: var(--accent-color-1);
		font-variation-settings: 'FILL' 1;
		transition:
			0.2s,
			outline 0s;
	}

	@media screen and (max-width: 768px) {
		.choice-input {
			margin-top: 0em;
		}
	}
</style>
