<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let questionIndex: number;
</script>

<div class="choice-area display binary">
	<label
		title={$t('select_answer')}
		class="choice binary"
		class:selected={$answers[questionIndex].choices[0] === $questions[questionIndex].choices[0]}
		><div class="icon">
			<input
				type="radio"
				name={questionIndex.toString()}
				on:change={() => {
					$answers[questionIndex].choices[0] = $questions[questionIndex].choices[0];
				}}
			/>
			<i class="symbol">thumb_up</i>
		</div>
		<div class="choice-input display binary">
			{$questions[questionIndex].choices[0]}
		</div>
	</label>
	<label
		title={$t('select_answer')}
		class="choice binary"
		class:selected={$answers[questionIndex].choices[0] === $questions[questionIndex].choices[1]}
		><div class="icon">
			<input
				type="radio"
				name={questionIndex.toString()}
				on:change={() => {
					$answers[questionIndex].choices[0] = $questions[questionIndex].choices[1];
				}}
			/>
			<i class="symbol">thumb_down</i>
		</div>
		<div class="choice-input display binary">
			{$questions[questionIndex].choices[1]}
		</div>
	</label>
</div>

<style>
	.choice {
		cursor: pointer;
	}

	.choice-input {
		margin-top: 0.5em;
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
