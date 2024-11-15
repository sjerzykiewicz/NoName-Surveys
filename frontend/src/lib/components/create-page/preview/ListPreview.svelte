<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);
	import Tx from 'sveltekit-translate/translate/tx.svelte';

	export let questionIndex: number;
</script>

<div class="choice-area display" transition:slide={{ duration: 200, easing: cubicInOut }}>
	<select title={$t('select_answer')} name={questionIndex.toString()}>
		<option value="" disabled selected hidden><Tx text="select_answer" /></option>
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
