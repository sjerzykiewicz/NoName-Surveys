<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';

	export let questionIndex: number;

	$answers[questionIndex].choices[0] = $questions[questionIndex].choices[0];
</script>

<div class="choice-area display">
	<select
		title="Select your answer"
		name={questionIndex.toString()}
		bind:value={$answers[questionIndex].choices[0]}
	>
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
		background-color: var(--primary-color);
		padding: 0.25em;
		border: 1px solid var(--border-color);
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--shadow-color);
		font-size: 1em;
		cursor: pointer;
		font-weight: normal;
		color: var(--text-color);
		max-width: calc(100% - 2.25em);
		transition: 0.2s;
		overflow-wrap: break-word;
		text-overflow: ellipsis;
	}
</style>
