<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	export let questionIndex: number;
</script>

<div
	title="Question no. {questionIndex + 1}"
	class="question-area display"
	in:slide={{ duration: 200, easing: cubicInOut }}
	out:slide={{ delay: 200, duration: 200, easing: cubicInOut }}
>
	<div class="index">{questionIndex + 1}.</div>
	<div class="question-title">
		{$questions[questionIndex].question}
		{#if $questions[questionIndex].required}
			<i title="Required" class="material-symbols-rounded">asterisk</i>
		{/if}
	</div>
</div>
