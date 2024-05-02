<script lang="ts">
	import { questions, answers } from '$lib/stores/fill-page';
	export let questionIndex: number;

	$answers[questionIndex].choices[0] = $questions[questionIndex].choices[0];
</script>

<div class="choice-area">
	<select name={$questions[questionIndex].question} bind:value={$answers[questionIndex].choices[0]}>
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
		flex: 1;
		background-color: var(--secondary-color);
		padding: 0.25em;
		border: 1px solid var(--border-color);
		border-radius: 5px;
		box-shadow: 0px 4px 4px var(--box-shadow-color);
		font-size: 1.25em;
		cursor: text;
		margin-right: 0.5em;
		font-size: 1em;
		font-weight: normal;
		font-family: 'Jura';
		color: var(--text-color);
	}

	@media screen and (max-width: 767px) {
		select,
		option {
			font-size: 1em;
		}
	}
</style>
