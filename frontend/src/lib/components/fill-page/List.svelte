<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';

	export let questionIndex: number;

	$answers[questionIndex].choices[0] = '';
</script>

<div class="choice-area display">
	<select
		title="Select your answer"
		name={questionIndex.toString()}
		bind:value={$answers[questionIndex].choices[0]}
	>
		<option value="" disabled selected hidden>Select your answer</option>
		{#each $questions[questionIndex].choices as choice}
			<option value={choice}>
				{choice}
			</option>
		{/each}
	</select>
</div>

<style>
	.choice-area {
		margin-left: 2.25em;
	}

	select {
		cursor: pointer;
		max-width: calc(100% - 2.25em);
		overflow-wrap: break-word;
		text-overflow: ellipsis;
	}
</style>
