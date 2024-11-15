<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let questionIndex: number;

	let checked: number;
</script>

<div class="choice-area display" transition:slide={{ duration: 200, easing: cubicInOut }}>
	{#each $questions[questionIndex].choices as choice, choiceIndex}
		<label title={$t('select_answer')} class="choice">
			<div class="radio">
				<input
					type="radio"
					name={questionIndex.toString()}
					on:change={() => {
						checked = choiceIndex;
					}}
				/>
			</div>
			<div class="choice-input display" class:selected={checked === choiceIndex}>
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
