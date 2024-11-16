<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';
	import Input from '$lib/components/global/Input.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);
	export let questionIndex: number;

	$answers[questionIndex].choices[0] = '';
</script>

<div class="choice-area text display">
	<div title={$t('question_details')} class="details">
		{$questions[questionIndex].choices[0]}
	</div>
	<Input
		bind:text={$answers[questionIndex].choices[0]}
		label={$t('answer')}
		title={$t('enter_answer')}
		--margin-right="0em"
	/>
</div>
