<script lang="ts">
	import { questions } from '$lib/stores/create-page';

	export let questionIndex: number;

	$questions[questionIndex].choices[1] = '';
</script>

<div class="choice-area display">
	<div title="Question details" class="details">
		{$questions[questionIndex].choices[0]}
	</div>
	<div
		title="Enter your answer"
		class="text-area"
		contenteditable
		bind:textContent={$questions[questionIndex].choices[1]}
	>
		{$questions[questionIndex].choices[1]}
	</div>
</div>

<style>
	.text-area[contenteditable]:empty::before {
		content: 'Enter your answer...';
	}
</style>
