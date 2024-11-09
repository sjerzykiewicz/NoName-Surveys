<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';
	import Input from '$lib/components/global/Input.svelte';

	export let questionIndex: number;

	$answers[questionIndex].choices[0] = '';
</script>

<div class="choice-area text display">
	<div title="Question details" class="details">
		{$questions[questionIndex].choices[0]}
	</div>
	<Input
		bind:text={$answers[questionIndex].choices[0]}
		label="Answer"
		title="Enter your answer"
		--margin-right="0em"
	/>
</div>
