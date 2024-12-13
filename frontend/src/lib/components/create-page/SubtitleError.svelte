<script lang="ts">
	import { SurveyError } from '$lib/entities/SurveyError';
	import { questions } from '$lib/stores/create-page';
	import { LIMIT_OF_CHARS } from '$lib/stores/global';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let questionIndex: number;

	function errorMessage() {
		return $t('subtitle_error', { limit: $LIMIT_OF_CHARS });
	}

	$: checkSubtitleError = (i: number) => {
		const q = $questions[i].question;
		return $questions[i].error === SurveyError.SubtitleTooLong && q.length > $LIMIT_OF_CHARS;
	};
</script>

<div transition:slide={{ duration: 200, easing: cubicInOut }}>
	{#if checkSubtitleError(questionIndex)}
		<p title={$t('error')} class="error" transition:slide={{ duration: 200, easing: cubicInOut }}>
			<i class="symbol">error</i>
			{#key [$t, $questions[questionIndex].error]}
				{errorMessage()}
			{/key}
		</p>
	{/if}
</div>

<style>
	.error {
		margin-top: -0.75em;
		margin-bottom: 0.5em;
		margin-left: 2.8em;
	}
</style>
