<script lang="ts">
	import Input from '$lib/components/global/Input.svelte';
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);
	export let questionIndex: number;

	let text: string = '';
</script>

<div class="choice-area text display" transition:slide={{ duration: 200, easing: cubicInOut }}>
	<div title={$t('question_details')} class="details">
		{$questions[questionIndex].choices[0]}
	</div>
	<Input bind:text label={$t('answer')} title={$t('enter_answer')} --margin-right="0em" />
</div>
