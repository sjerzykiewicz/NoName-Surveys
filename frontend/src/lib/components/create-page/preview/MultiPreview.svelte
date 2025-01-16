<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let questionIndex: number;

	let selected: Array<boolean> = [];

	for (let i = 0; i < $questions[questionIndex].choices.length; i++) {
		selected[i] = false;
	}
</script>

<div class="choice-area display" transition:slide={{ duration: 200, easing: cubicInOut }}>
	{#each $questions[questionIndex].choices as choice, choiceIndex}
		<label title={$t('select_answer')} class="choice">
			<div class="checkbox">
				<input
					type="checkbox"
					on:change={() => {
						selected[choiceIndex] = !selected[choiceIndex];
					}}
				/>
			</div>
			<div class="choice-input display" class:selected={selected[choiceIndex]}>
				{choice}
			</div>
		</label>
	{/each}
</div>

<style>
	.choice {
		cursor: pointer;
	}
</style>
