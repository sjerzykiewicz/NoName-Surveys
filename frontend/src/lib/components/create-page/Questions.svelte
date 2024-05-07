<script lang="ts">
	import QuestionButtons from '$lib/components/create-page/QuestionButtons.svelte';
	import QuestionTitle from '$lib/components/create-page/QuestionTitle.svelte';
	import { questions, questionErrors } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	function scrollToElement(selector: string) {
		const element = document.querySelector(selector) as HTMLElement;

		if (element) {
			element.scrollIntoView({ behavior: 'smooth' });
		}
	}
</script>

{#each $questions as question, questionIndex}
	<div
		class="question"
		in:slide={{ duration: 200, easing: cubicInOut }}
		on:introend={() => scrollToElement('.add-question')}
	>
		<QuestionTitle {questionIndex} />
		<svelte:component this={question.component} {questionIndex} />
	</div>
	{#if $questionErrors.includes(questionIndex)}
		<p class="error">
			<i class="material-symbols-rounded">error</i>Please fill out or remove question {questionIndex +
				1}.
		</p>
	{/if}
{/each}
<QuestionButtons />

<style>
	.question {
		margin-bottom: 1.875em;
	}

	.error {
		padding-left: 2em;
		margin: -1em 0em 1em 0em;
	}

	@media screen and (max-width: 767px) {
		.error {
			font-size: 1em;
		}
	}
</style>
