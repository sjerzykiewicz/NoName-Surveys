<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';
	import Input from '$lib/components/global/Input.svelte';
	import { getContext } from 'svelte';
	import { CONTEXT_KEY, type SvelteTranslate } from 'sveltekit-translate/translate/translateStore';

	const { t } = getContext<SvelteTranslate>(CONTEXT_KEY);

	export let questionIndex: number;
	export let questionInput: HTMLDivElement;

	function moveQuestionUp() {
		const higher = $questions[questionIndex];
		$questions[questionIndex] = $questions[questionIndex - 1];
		$questions[questionIndex - 1] = higher;
	}

	function moveQuestionDown() {
		const lower = $questions[questionIndex];
		$questions[questionIndex] = $questions[questionIndex + 1];
		$questions[questionIndex + 1] = lower;
	}

	function removeQuestion() {
		$questions.splice(questionIndex, 1);
		$questions = $questions;
	}
</script>

<div class="question-area subtitle" transition:slide={{ duration: 200, easing: cubicInOut }}>
	<div class="arrows">
		<button
			title={$t('subtitle_up')}
			class="up"
			disabled={questionIndex === 0}
			on:click={moveQuestionUp}
		>
			<i class="symbol">keyboard_arrow_up</i>
		</button>
		<button
			title={$t('subtitle_down')}
			class="down"
			disabled={questionIndex === $questions.length - 1}
			on:click={moveQuestionDown}
		>
			<i class="symbol">keyboard_arrow_down</i>
		</button>
	</div>
	<Input
		bind:text={$questions[questionIndex].question}
		label={$t('subtitle')}
		title={$t('subtitle_title')}
		bind:element={questionInput}
	/>
	<button title={$t('subtitle_remove')} class="remove-question" on:click={removeQuestion}>
		<i class="symbol">delete</i>
	</button>
</div>
