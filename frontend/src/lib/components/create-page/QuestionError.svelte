<script lang="ts">
	import { QuestionError } from '$lib/entities/QuestionError';
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	export let questionIndex: number;

	function errorMessage(i: number) {
		return 'Please enter question no. ' + (i + 1) + '.';
	}

	$: checkQuestionError = (i: number) => {
		const q = $questions[i].question;
		return (
			$questions[i].error === QuestionError.QuestionRequired &&
			(q === null || q === undefined || q.length === 0)
		);
	};
</script>

{#if checkQuestionError(questionIndex)}
	<p
		title="Error"
		class="error question-error"
		transition:slide={{ duration: 200, easing: cubicInOut }}
	>
		<i class="material-symbols-rounded">error</i>{errorMessage(questionIndex)}
	</p>
{/if}

<style>
	.error {
		margin-left: 2.8em;
	}

	.question-error {
		margin-top: -0.5em;
		margin-bottom: 0.5em;
	}
</style>
