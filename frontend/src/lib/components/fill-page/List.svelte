<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';
	import Tx from 'sveltekit-translate/translate/tx.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let questionIndex: number;

	$answers[questionIndex].choices[0] = '';
</script>

<div class="choice-area display">
	<select title={$t('select_answer')} bind:value={$answers[questionIndex].choices[0]}>
		<option value="" selected><Tx text="select_no_answer" /></option>
		{#each $questions[questionIndex].choices as choice}
			<option value={choice}>
				{choice}
			</option>
		{/each}
	</select>
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
</style>
