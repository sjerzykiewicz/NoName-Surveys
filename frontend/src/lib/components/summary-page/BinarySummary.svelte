<script lang="ts">
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let data: { answers: string[]; choices: string[] };

	function calculatePercentage(answer: string, answers: string[]) {
		return ((answers.filter((a) => a === answer).length / answers.length) * 100).toFixed(2);
	}
</script>

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
			{calculatePercentage(data.choices[0], data.answers)}%
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
			{calculatePercentage(data.choices[1], data.answers)}%
		</div>
	</label>
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
	}
</style>
