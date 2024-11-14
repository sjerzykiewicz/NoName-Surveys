<script lang="ts">
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let data: { answer: string; details: string };
</script>

<div class="choice-area text display">
	<div title="Question details" class="details">
		{data.details}
	</div>
	<div title={$t('answer')} class="text-input display">
		{data.answer}
	</div>
</div>

<style>
	.text-input {
		border: 1px solid var(--accent-color-1);
		background-color: var(--secondary-color-2);
		color: var(--accent-color-1);
		transition:
			0.2s,
			outline 0s;
	}
</style>
