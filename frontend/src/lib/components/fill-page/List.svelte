<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);
	import Tx from 'sveltekit-translate/translate/tx.svelte';

	export let questionIndex: number;

	$answers[questionIndex].choices[0] = '';
</script>

<div class="choice-area display">
	<select
		title={$t('select_answer')}
		name={questionIndex.toString()}
		bind:value={$answers[questionIndex].choices[0]}
	>
		<option value="" disabled selected hidden><Tx text="select_answer" /></option>
		{#each $questions[questionIndex].choices as choice}
			<option value={choice}>
				{choice}
			</option>
		{/each}
	</select>
	{#if $answers[questionIndex].choices[0] !== ''}
		<div class="clear-answer">
			<button
				title={$t('clear-answer_title')}
				on:click={() => ($answers[questionIndex].choices[0] = '')}
				><Tx text="clear-answer" /></button
			>
		</div>
	{/if}
</div>

<style>
	.choice-area {
		margin-left: 2.25em;
	}

	select {
		cursor: pointer;
		max-width: calc(100% - 2.25em);
		overflow-wrap: break-word;
		text-overflow: ellipsis;
	}

	.clear-answer {
		justify-content: flex-start;
	}
</style>
