<script lang="ts">
	import { SurveyError } from '$lib/entities/SurveyError';
	import { questions } from '$lib/stores/create-page';
	import { LIMIT_OF_CHARS } from '$lib/stores/global';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	export let questionIndex: number;

	function errorMessage(i: number) {
		const error = $questions[i].error;
		switch (error) {
			case SurveyError.QuestionRequired:
				return 'Please enter question no. ' + (i + 1) + '.';
			case SurveyError.QuestionTooLong:
				return (
					'Question no. ' + (i + 1) + ' must be ' + $LIMIT_OF_CHARS + ' or less characters long.'
				);
		}
	}

	$: checkQuestionError = (i: number) => {
		const q = $questions[i].question;
		const error = $questions[i].error;
		switch (error) {
			case SurveyError.QuestionRequired:
				return q === null || q === undefined || q.trim().length === 0;
			case SurveyError.QuestionTooLong:
				return q.length > $LIMIT_OF_CHARS;
		}
	};
</script>

<div
	in:slide={{ delay: 200, duration: 200, easing: cubicInOut }}
	out:slide={{ duration: 200, easing: cubicInOut }}
>
	{#if checkQuestionError(questionIndex)}
		<p title="Error" class="error" transition:slide={{ duration: 200, easing: cubicInOut }}>
			<i class="symbol">error</i>{errorMessage(questionIndex)}
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
