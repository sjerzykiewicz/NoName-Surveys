<script lang="ts">
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);
	export let data: { answer: string[] };
</script>

<div class="choice-area display">
	{#each data.answer as answer, answerIndex}
		<div title="{$t('answer_no')} {answerIndex + 1}" class="choice">
			<div class="rank">{answerIndex + 1}.</div>
			<div class="choice-input display">
				{answer}
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
