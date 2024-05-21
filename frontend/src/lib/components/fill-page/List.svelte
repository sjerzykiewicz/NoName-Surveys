<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';

	export let questionIndex: number;

	$answers[questionIndex].choices[0] = $questions[questionIndex].choices[0];
</script>

<div class="choice-area">
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
		padding-left: 2.3em;
	}

	select {
		background-color: var(--primary-color);
		padding: 0.25em;
		border: 1px solid var(--border-color);
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--shadow-color);
		font-size: 1.25em;
		cursor: pointer;
		font-weight: normal;
		color: var(--text-color);
		max-width: 100%;
		transition: 0.2s;
		overflow-wrap: break-word;
		text-overflow: ellipsis;
	}

	@media screen and (max-width: 767px) {
		select {
			font-size: 1.5em;
		}
	}
</style>
