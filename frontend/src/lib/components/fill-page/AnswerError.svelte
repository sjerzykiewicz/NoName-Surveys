<script lang="ts">
	import { answers } from '$lib/stores/fill-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import { questions } from '$lib/stores/fill-page';

	export let unansweredRequired: Array<number>;
	export let questionIndex: number;

	function errorMessage(i: number) {
		return 'Please answer question no. ' + (i + 1) + '.';
	}

	$: checkAnswerError = (i: number) => {
		return (
			unansweredRequired.includes(questionIndex) &&
			($answers[i].choices.length === 0 ||
				$answers[i].choices.some((c) => c === null || c === undefined || c.trim().length === 0))
		);
	};
</script>

<div
	in:slide={{ delay: 200, duration: 200, easing: cubicInOut }}
	out:slide={{ duration: 200, easing: cubicInOut }}
>
	{#if checkAnswerError(questionIndex)}
		<p
			title="Error"
			class="error"
			style={$questions[questionIndex].type === 'text' ? 'margin-top: -2.5em;' : ''}
			transition:slide={{ duration: 200, easing: cubicInOut }}
		>
			<i class="material-symbols-rounded">error</i>{errorMessage(questionIndex)}
		</p>
	{/if}
</div>

<style>
	.error {
		margin: -1em 0em 0.5em 2.8em;
	}
</style>
