<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	export let questionIndex: number;
</script>

<div
	class="question-area subtitle display"
	class:empty={$questions[questionIndex].question === ''}
	transition:slide={{ duration: 200, easing: cubicInOut }}
>
	<div class="question-title">
		{$questions[questionIndex].question}
	</div>
</div>
