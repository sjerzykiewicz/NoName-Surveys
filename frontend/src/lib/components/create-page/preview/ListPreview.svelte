<script lang="ts">
	import { questions } from '$lib/stores/create-page';
	import { cubicInOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	export let questionIndex: number;
</script>

<div class="choice-area display" transition:slide={{ duration: 200, easing: cubicInOut }}>
	<select title="Select your answer" name={questionIndex.toString()}>
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
