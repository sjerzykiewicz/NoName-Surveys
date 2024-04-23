<script lang="ts">
	import QuestionButtons from '$lib/components/QuestionButtons.svelte';
	import QuestionTitle from '$lib/components/QuestionTitle.svelte';
	import { questions } from '$lib/stores';
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
		in:slide={{ duration: 300, easing: cubicInOut }}
		on:introend={() => scrollToElement('.button-group')}
	>
		<QuestionTitle {questionIndex} />
		<svelte:component this={question.component} {questionIndex} />
	</div>
{/each}
<QuestionButtons />

<style>
	.question {
		margin-bottom: 2em;
	}
</style>
