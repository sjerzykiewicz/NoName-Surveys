<script lang="ts">
	import { answers } from '$lib/stores/fill-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let unansweredRequired: Set<number>;
	export let questionIndex: number;

	function errorMessage(i: number) {
		return $t('answer_question_no') + (i + 1) + '.';
	}

	$: checkAnswerError = (i: number) => {
		return (
			unansweredRequired.has(questionIndex) &&
			($answers[i].choices.length === 0 ||
				$answers[i].choices.some((c) => c === null || c === undefined || c.trim().length === 0))
		);
	};
</script>

{#if checkAnswerError(questionIndex)}
	<p title={$t('error')} class="error" transition:slide={{ duration: 200, easing: cubicInOut }}>
		<i class="symbol">error</i>{errorMessage(questionIndex)}
	</p>
{/if}

<style>
	.error {
		margin: var(--margin-top, -1em) 0em 0.5em 2.8em;
	}
</style>
