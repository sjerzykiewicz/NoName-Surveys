<script lang="ts">
	import { questions } from '$lib/stores/create-page';

	export let questionIndex: number;
</script>

<div class="choice-area display">
	<select title="Select your answer" name={questionIndex.toString()}>
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
